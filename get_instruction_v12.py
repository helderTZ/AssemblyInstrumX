from instruction_id_v10 import *
from instruction_counter import *

import re


def divideIntoBlocks():
    
    f_instructions = open('instructions.txt', 'r')
    f_opcodes = open('opcodes.txt', 'r')
    
    line_instructions = f_instructions.readlines()
    lines_opcodes = f_opcodes.readlines()
    new_text_opcodes = ''
    
    opcodeIdx = 0
    for l in range(len(line_instructions)):
        line = line_instructions[l]
        if line[0:5] == 'Block':
            new_text_opcodes += '\n'
        else:
            new_text_opcodes += lines_opcodes[opcodeIdx]
            opcodeIdx += 1
        
    f_instructions.close()
    f_opcodes.close()
    f_new_opcodes = open('opcodes.txt', 'w')
    print(new_text_opcodes, file=f_new_opcodes)
    f_new_opcodes.close()
    

def bitsSuffix(opcode):
    if opcode[-4:-1] == 'HPS' or opcode[-4:-1] == 'LPS' or opcode[-3:-1] == 'SS':
        return 32
    elif opcode[-4:-1] == 'HPD' or opcode[-4:-1] == 'LPD' or opcode[-3:-1] == 'SD':
        return 64
    elif opcode[-3:-1] == 'PS' or opcode[-3:-1] == 'PD':
        return 128
    else:
        return 0

def idOperands(operands):
    operIds = []
    for op in operands:
        if '(' in op:
            operIds.append('MEM')
        elif op[0] == '$':
            operIds.append('IMM')
        else:
            operIds.append('REG')
    return operIds

def regSize(oper, operId):
    if operId == 'MEM':
        return -1
    else:
        reg = oper[0:]
    if reg[0] == 'r':
        return 64
    elif reg[0] == 'e':
        return 32
    elif reg[0] == 'x':
        return 128
    elif reg[0] == 'y':
        return 256
    elif reg[0] == 'z':
        return 512
    else:
        return -1

def idSuffixBits(suff):
    if suff == 'B':      # byte
        return 8
    elif suff == 'W':    # word
        return 16
    elif suff == 'D':    # double word
        return 32
    elif suff == 'Q':    # quad word
        return 64
    elif suff == 'X':
        return 128
    elif suff == 'Y':
        return 256
    elif suff == 'Z':
        return 512
    else:
        return -1

def dumpList(l,f):
    for item in l:
        print(item.show(), file=f)
        
def dumpSet(s,f):
    for item in s:
        item.deep_show(f)

def dumpAll():
    with open('debug1.txt', 'w') as f:
        dumpList(instructions, f)
    with open('debug2.txt', 'w') as f:
        dumpSet(instructionSets, f)
        
    
[instructionSets, instructions] = fill_instruction_database()
instructionNames = get_instruction_names(instructions)


# DEBUG
dumpAll()


opcodes = []
labels = []
insSets = []
dataModes = []
dataTypes = []
dataTraffic = []
suffixes = []

blocks = []

pattern = r"<Block [1-9]>"

with open('instructions.txt') as f:

    lines = f.readlines()
    lineIdx = 0
    
    for line in lines:
        
        # skip empty lines
        if line == []:
            continue
        
        lineIdx += 1
        # skip lines with Block #:
        if line[0:5] == 'Block':
            blocks.append(lineIdx)
            continue
        
        regs = []
        instruction = line.split()
        
        if 'hint-taken' in instruction:
            instruction.remove('hint-taken')
        
        # check if NOP
        if 'nop' in instruction:
            opcode = 'NOP'
        else:
            opcode = instruction[0].upper()
        opcodes.append(opcode)
        operands = instruction[1:]
        # delete <Block #> from operands of BRANCH instructions
        if re.search(pattern, line):
            operands = operands[:-2]
        # clean
        for op in range(len(operands)):
            operands[op] = operands[op].replace(',', '')
            operands[op] = operands[op].replace('%', '')
        
        

        # first we need to check if the opcode has a suffix or not
        hasSuffix = None
        suffix = ''
        if opcode in instructionNames:
            hasSuffix = False
        elif opcode[:-1] in instructionNames:
            hasSuffix = True
            suffix = opcode[-1]
            opcode = opcode[:-1]
        elif opcode[:-2] in instructionNames:
            hasSuffix = True
            suffix = opcode[-2:-1]
            opcode = opcode[:-2]
        suffixes.append(hasSuffix)

        identified = False
        labeled = False
        label = ''
        
        # search opcode in instructions list
        for ins in instructions:
            
            if opcode == ins.opcode:
                
                insSet = ins.set.name
                if insSet[0:3] == 'SSE':
                    insSet = 'SSE'
                if insSet[0:3] == 'FMA':
                    insSet = 'AVX'
                    
                operIds = idOperands(operands)
                for op, opId in zip(operands, operIds):
                    if opId == 'REG':
                        regs.append(op)
                        
                possibleLabels = ins.labels
                        
                if opcode == 'MOVSD':
                     # there are two MOVSD isntructions
                     # decide based on operands
                    if len(operIds) == 2 and (regSize(operands[0], operIds[0]) > 64 or regSize(operands[1], operIds[1]) > 64):
                        if insSet == 'X86': # continue for it will find SSE2 eventually
                            continue
                        
                if len(possibleLabels) == 1:
                    label = possibleLabels[0]
                    labels.append(possibleLabels[0])
                    labeled = True
                    
                elif len(possibleLabels) > 1:
                    
                    uOp = False
                    label = ''
                    for l in possibleLabels:
                        if '+' in l and ('LD' in l or 'ST' in l):
                            if 'MEM' in operIds:
                                label = l
                                uOp = True
                        else:
                            label = l
                    if label != '' and not ('LD' in possibleLabels and 'ST' in possibleLabels and 'MOV' in possibleLabels):
                        labels.append(label)
                        labeled = True
                        
                    else:
                        
                        if possibleLabels[0] == 'LD' or possibleLabels[0] == 'ST':
                            # decide based on operands
                            if len(operIds) >= 2 and operIds[0] == 'MEM' and operIds[1] == 'REG':
                                label = 'LD'
                                labels.append('LD')
                                labeled = True
                            elif len(operIds) >= 2 and operIds[0] == 'REG' and operIds[1] == 'MEM':
                                label = 'ST'
                                labels.append('ST')
                                labeled = True
                            elif len(operIds) >= 2 and operIds[0] == 'REG' and operIds[1] == 'REG':
                                label = 'MOV'
                                labels.append('MOV')
                                labeled = True
                            elif len(operIds) >= 2 and operIds[0] == 'IMM' and operIds[1] == 'REG':
                                label = 'MOV'
                                labels.append('MOV')
                                labeled = True
                                
                        elif len(operands) == 4:
                            # decide based on operands
                            if len(operIds) >= 2 and operIds[1] == 'MEM' and operIds[2] == 'REG':
                                labels.append('LD')
                                labeled = True
                            elif len(operIds) >= 2 and operIds[2] == 'REG' and operIds[3] == 'REG':
                                labels.append('MOV')
                                labeled = True
                                
                        else:
                            labels.append('?')
                            labeled = True
                    
                # check transfered bits
                if ins.dataTraffic != None and ins.dataTraffic != 'R' and 'MEM' in operIds:
                    dataTraffic.append(ins.dataTraffic)
                elif (label != 'LD' and label != 'ST') and not ('LD+' in label or 'ST+' in label):
                    dataTraffic.append('N/A')
                elif hasSuffix:
                    bits = idSuffixBits(suffix)
                    dataTraffic.append(str(bits))
                else:
                    bits = bitsSuffix(opcode)
                    if bits == 0:   # need to check operands
                        if possibleLabels[0] != 'BRANCH':
                            minSize = 999
                            if len(operands) > 1:
                                for reg in regs:
                                    size = regSize(reg, 'REG')
                                    if size == -1:
                                        print(line)
                                        print(regs)
                                    if size < minSize:
                                        minSize = size
                            dataTraffic.append(str(minSize))
                        else:
                            dataTraffic.append('N/A')
                    else:
                        dataTraffic.append(bits)
                    
                insSets.append(insSet)
                dataModes.append(ins.dataMode)
                dataTypes.append(ins.dataType)
                identified = True
                break
        
        # DEBUG
        if identified == False:
            print(opcode + '\t' + str(suffix))
        if labeled == False:
            print(line, end='')
            print(opcode + '\t' + str(possibleLabels) + '\t' + str(operIds))

# DEBUG
print('opcodes: ' + '\t' + str(len(opcodes)))
print('labels: ' + '\t' + str(len(labels)))
print('sets: ' + '\t' + str(len(insSets)))
print('data modes:' + '\t' + str(len(dataModes)))
print('data types:' + '\t' + str(len(dataTypes)))
print('suffixes: ' + '\t' + str(len(suffixes)))
print('bytes: ' + '\t' + str(len(dataTraffic)))



f = open('opcodes.txt', 'w')
line = ''
for i in range(len(opcodes)):
    #line = opcodes[i] + '\t' + labels[i] + '\t' + str(insSets[i]) + '\t' + str(dataModes[i]) + '\t'+ str(dataTypes[i]) + '\t' + str(dataTraffic[i])
    line = labels[i] + '\t' + str(insSets[i]) +'\t' + str(dataModes[i]) + '\t'+ str(dataTypes[i]) + '\t' + str(dataTraffic[i])
    print(line, file=f)
    f.flush()
f.close()

divideIntoBlocks()

printInstructionMix(opcodes, labels, insSets, dataModes, dataTypes)
