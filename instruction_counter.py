


def countOpcodes(opcodes):
    op_count = {}
    for op in opcodes:
        if op not in op_count:
            op_count[op] = 1
        else:
            op_count[op] += 1
    return op_count



def countIns(labels, insSets, dataModes, dataTypes):
    ins_count = {}
    dpfp_scalar_ins_count = {}
    dpfp_vector_ins_count = {}
    dpfp_others_ins_count = {}
    spfp_scalar_ins_count = {}
    spfp_vector_ins_count = {}
    spfp_others_ins_count = {}
    int_scalar_ins_count = {}
    int_vector_ins_count = {}
    int_others_ins_count = {}
    others_ins_count = {}
    
    compute = {}
    memory = {}
    compMem = {}

    for i in range(len(labels)):
        label = labels[i]
        key = dataTypes[i] +'\t' + dataModes[i] +'\t' + insSets[i] +'\t' + label

        if key not in ins_count:
            ins_count[key] = 1
            
            if 'LD' in label or 'ST' in label:
                if '+' in label:
                    compMem[key] = 1
                else:
                    memory[key] = 1
            else:
                compute[key] = 1
            
            if dataTypes[i] == 'DP FP' and dataModes[i] == 'SCALAR':
                dpfp_scalar_ins_count[key] = 1
            elif dataTypes[i] == 'DP FP' and dataModes[i] == 'SIMD':
                dpfp_vector_ins_count[key] = 1
            elif dataTypes[i] == 'DP FP' and dataModes[i] == 'N/A':
                dpfp_others_ins_count[key] = 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'SCALAR':
                spfp_scalar_ins_count[key] = 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'SIMD':
                spfp_vector_ins_count[key] = 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'N/A':
                spfp_others_ins_count[key] = 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'SCALAR':
                int_scalar_ins_count[key] = 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'SIMD':
                int_vector_ins_count[key] = 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'N/A':
                int_others_ins_count[key] = 1
            else:
                others_ins_count[key] = 1
        else:
            ins_count[key] += 1
            
            if 'LD' in label or 'ST' in label:
                if '+' in label:
                    compMem[key] += 1
                else:
                    memory[key] += 1
            else:
                compute[key] += 1
            
            if dataTypes[i] == 'DP FP' and dataModes[i] == 'SCALAR':
                dpfp_scalar_ins_count[key] += 1
            elif dataTypes[i] == 'DP FP' and dataModes[i] == 'SIMD':
                dpfp_vector_ins_count[key] += 1
            elif dataTypes[i] == 'DP FP' and dataModes[i] == 'N/A':
                dpfp_others_ins_count[key] += 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'SCALAR':
                spfp_scalar_ins_count[key] += 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'SIMD':
                spfp_vector_ins_count[key] += 1
            elif dataTypes[i] == 'SP FP' and dataModes[i] == 'N/A':
                spfp_others_ins_count[key] += 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'SCALAR':
                int_scalar_ins_count[key] += 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'SIMD':
                int_vector_ins_count[key] += 1
            elif dataTypes[i] == 'INT' and dataModes[i] == 'N/A':
                int_others_ins_count[key] += 1
            else:
                others_ins_count[key] += 1
        
    

    return [ins_count, dpfp_scalar_ins_count, dpfp_vector_ins_count, spfp_scalar_ins_count, spfp_vector_ins_count, int_scalar_ins_count, int_vector_ins_count, others_ins_count, compute, memory, compMem]



def printInstructionMixByType(opcodes, labels, insSets, dataModes, dataTypes):
    
    [ins_count, dpfp_scalar_ins_count, dpfp_vector_ins_count, spfp_scalar_ins_count, spfp_vector_ins_count, int_scalar_ins_count, int_vector_ins_count, others_ins_count, compute, memory, compMem] = countIns(labels, insSets, dataModes, dataTypes)
    with open('inst_counter_by_type.txt', 'w') as f:
    
        print('DP FP:', file=f)
        for key, value in dpfp_vector_ins_count.items():
            print('\t' + key[6:] + '\t'+ str(value), file=f)
        for key, value in dpfp_scalar_ins_count.items():
            print('\t' + key[6:] +'\t' +str(value), file=f)
        print('SP FP:', file=f)
        for key, value in spfp_vector_ins_count.items():
            print('\t' + key[6:] +'\t' + str(value), file=f)
        for key, value in spfp_scalar_ins_count.items():
            print('\t' + key[6:] +'\t' + str(value), file=f)
        print('INT:', file=f)
        for key, value in int_vector_ins_count.items():
            print('\t' + key[4:] +'\t' + str(value), file=f)
        for key, value in int_scalar_ins_count.items():
            print('\t' + key[4:] +'\t' + str(value), file=f)
        print('OTHERS:', file=f)
        for key, value in others_ins_count.items():
            print('\t' + key +'\t' + str(value), file=f)
        
        


def printInstructionMix(opcodes, labels, insSets, dataModes, dataTypes):
    
    # DEBUG
    op_count = countOpcodes(opcodes)
    with open('opcode_counter.txt', 'w') as f:
        for op in op_count:
            print(op + '\t' + str(op_count[op]), file=f)
    
    # DEBUG
    printInstructionMixByType(opcodes, labels, insSets, dataModes, dataTypes)
        
    [ins_count, dpfp_scalar_ins_count, dpfp_vector_ins_count, spfp_scalar_ins_count, spfp_vector_ins_count, int_scalar_ins_count, int_vector_ins_count, others_ins_count, compute, memory, compMem] = countIns(labels, insSets, dataModes, dataTypes)
    with open('inst_counter.txt', 'w') as f:
        
        print('COMPUTE', file=f)
        for key in compute:
            if key in dpfp_vector_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] + '\t'+ str(dpfp_vector_ins_count[key]), file=f)
            elif key in dpfp_scalar_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(dpfp_scalar_ins_count[key]), file=f)
            elif key in spfp_vector_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_vector_ins_count[key]), file=f)
            elif key in spfp_scalar_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_scalar_ins_count[key]), file=f)
            elif key in int_vector_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_vector_ins_count[key]), file=f)
            elif key in int_scalar_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_scalar_ins_count[key]), file=f)
            elif key in others_ins_count:
                print('\tOTHERS:', file=f)
                print('\t\t' + key[6:] +'\t' +str(others_ins_count[key]), file=f)
        
        print('MEMORY', file=f)
        for key in memory:
            if key in dpfp_vector_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] + '\t'+ str(dpfp_vector_ins_count[key]), file=f)
            elif key in dpfp_scalar_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(dpfp_scalar_ins_count[key]), file=f)
            elif key in spfp_vector_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_vector_ins_count[key]), file=f)
            elif key in spfp_scalar_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_scalar_ins_count[key]), file=f)
            elif key in int_vector_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_vector_ins_count[key]), file=f)
            elif key in int_scalar_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_scalar_ins_count[key]), file=f)
            elif key in others_ins_count:
                print('\tOTHERS:', file=f)
                print('\t\t' + key[6:] +'\t' +str(others_ins_count[key]), file=f)
        
        print('MEMORY+COMPUTE', file=f)
        for key in compMem:
            if key in dpfp_vector_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] + '\t'+ str(dpfp_vector_ins_count[key]), file=f)
            elif key in dpfp_scalar_ins_count:
                print('\tDP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(dpfp_scalar_ins_count[key]), file=f)
            elif key in spfp_vector_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_vector_ins_count[key]), file=f)
            elif key in spfp_scalar_ins_count:
                print('\tSP FP:', file=f)
                print('\t\t' + key[6:] +'\t' +str(spfp_scalar_ins_count[key]), file=f)
            elif key in int_vector_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_vector_ins_count[key]), file=f)
            elif key in int_scalar_ins_count:
                print('\tINT:', file=f)
                print('\t\t' + key[6:] +'\t' +str(int_scalar_ins_count[key]), file=f)
            elif key in others_ins_count:
                print('\tOTHERS:', file=f)
                print('\t\t' + key[6:] +'\t' +str(others_ins_count[key]), file=f)


