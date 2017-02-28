

def sort_instructions():
    
    
    compute_labels = []
    memory_labels = []
    comp_mem_labels = []
    
    compute_list = []
    memory_list = []
    comp_mem_list = []
    others_list = []
    
    ordered_comp_list = []
    ordered_mem_list = []
    ordered_comp_mem_list = []
    ordered_others_list = []
    
    # populate lists
    with open('compute_list.txt') as f:
        lines = f.readlines()
        for line in lines:
            compute_labels.append(line[:-1])
    with open('memory_list.txt') as f:
        lines = f.readlines()
        for line in lines:
            memory_labels.append(line[:-1])
    for i in compute_list:
        comp_mem_labels.append('ST+'+i)
        comp_mem_labels.append('LD+'+i)
    
    # divide by COMP, MEM or COMP+MEM
    with open('opcodes.txt') as f:
        
        lines = f.readlines()
        for line in lines:
            
            if line == '\n':
                continue
            
            words = line.split('\t')
            words = words[:-1]
            if words[0] in compute_labels:
                compute_list.append('COMPUTE' + '\t' + '\t'.join(words))
            elif words[0] in memory_labels:
                memory_list.append('MEMORY' + '\t' + '\t'.join(words))
            elif words[0] in comp_mem_labels:
                comp_mem_list.append('COMP+MEM' + '\t' + '\t'.join(words))
            else:
                others_list.append('OTHERS' + '\t' + '\t'.join(words))
                
                
    
    # sort COMPUTE list by data type and SIMD/scalar
    dpfp_vector_indices = []
    dpfp_scalar_indices = []
    dpfp_others_indices = []
    spfp_vector_indices = []
    spfp_scalar_indices = []
    spfp_others_indices = []
    int_vector_indices = []
    int_scalar_indices = []
    int_others_indices = []
    others_indices = []
    for i in range(len(compute_list)):
        if   'DP FP' and 'SIMD'   in compute_list[i]: dpfp_vector_indices.append(i)
        elif 'DP FP' and 'SCALAR' in compute_list[i]: dpfp_scalar_indices.append(i)
        elif 'DP FP'              in compute_list[i]: dpfp_others_indices.append(i)
        elif 'SP FP' and 'SIMD'   in compute_list[i]: spfp_vector_indices.append(i)
        elif 'SP FP' and 'SCALAR' in compute_list[i]: spfp_scalar_indices.append(i)
        elif 'SP FP'              in compute_list[i]: spfp_others_indices.append(i)
        elif 'INT'   and 'SIMD'   in compute_list[i]: int_vector_indices.append(i)
        elif 'INT'   and 'SCALAR' in compute_list[i]: int_scalar_indices.append(i)
        elif 'INT'                in compute_list[i]: int_others_indices.append(i)
        else:                                         others_indices.append(i)
    for i in dpfp_vector_indices: ordered_comp_list.append(compute_list[i])
    for i in dpfp_scalar_indices: ordered_comp_list.append(compute_list[i])
    for i in dpfp_others_indices: ordered_comp_list.append(compute_list[i])
    for i in spfp_vector_indices: ordered_comp_list.append(compute_list[i])
    for i in spfp_scalar_indices: ordered_comp_list.append(compute_list[i])
    for i in spfp_others_indices: ordered_comp_list.append(compute_list[i])
    for i in int_vector_indices:  ordered_comp_list.append(compute_list[i])
    for i in int_scalar_indices:  ordered_comp_list.append(compute_list[i])
    for i in int_others_indices:  ordered_comp_list.append(compute_list[i])
    for i in others_indices:      ordered_comp_list.append(compute_list[i])
    
    # sort MEMORY list by data type and SIMD/scalar
    dpfp_vector_indices = []
    dpfp_scalar_indices = []
    dpfp_others_indices = []
    spfp_vector_indices = []
    spfp_scalar_indices = []
    spfp_others_indices = []
    int_vector_indices = []
    int_scalar_indices = []
    int_others_indices = []
    others_indices = []
    for i in range(len(memory_list)):
        if   'DP FP' and 'SIMD'   in memory_list[i]: dpfp_vector_indices.append(i)
        elif 'DP FP' and 'SCALAR' in memory_list[i]: dpfp_scalar_indices.append(i)
        elif 'DP FP'              in memory_list[i]: dpfp_others_indices.append(i)
        elif 'SP FP' and 'SIMD'   in memory_list[i]: spfp_vector_indices.append(i)
        elif 'SP FP' and 'SCALAR' in memory_list[i]: spfp_scalar_indices.append(i)
        elif  'SP FP'             in memory_list[i]: spfp_others_indices.append(i)
        elif 'INT'   and 'SIMD'   in memory_list[i]: int_vector_indices.append(i)
        elif 'INT'   and 'SCALAR' in memory_list[i]: int_scalar_indices.append(i)
        elif 'INT'                in memory_list[i]: int_others_indices.append(i)
        else:                                        others_indices.append(i)
    for i in dpfp_vector_indices: ordered_mem_list.append(memory_list[i])
    for i in dpfp_scalar_indices: ordered_mem_list.append(memory_list[i])
    for i in dpfp_others_indices: ordered_mem_list.append(memory_list[i])
    for i in spfp_vector_indices: ordered_mem_list.append(memory_list[i])
    for i in spfp_scalar_indices: ordered_mem_list.append(memory_list[i])
    for i in spfp_others_indices: ordered_mem_list.append(memory_list[i])
    for i in int_vector_indices:  ordered_mem_list.append(memory_list[i])
    for i in int_scalar_indices:  ordered_mem_list.append(memory_list[i])
    for i in int_others_indices:  ordered_mem_list.append(memory_list[i])
    for i in others_indices:      ordered_mem_list.append(memory_list[i])
        
        
    # sort COMPUTE+MEMORY list by data type and SIMD/scalar
    dpfp_vector_indices = []
    dpfp_scalar_indices = []
    dpfp_others_indices = []
    spfp_vector_indices = []
    spfp_scalar_indices = []
    spfp_others_indices = []
    int_vector_indices = []
    int_scalar_indices = []
    int_others_indices = []
    others_indices = []
    for i in range(len(comp_mem_list)):
        if   'DP FP' and 'SIMD'   in comp_mem_list[i]: dpfp_vector_indices.append(i)
        elif 'DP FP' and 'SCALAR' in comp_mem_list[i]: dpfp_scalar_indices.append(i)
        elif 'DP FP'              in comp_mem_list[i]: dpfp_others_indices.append(i)
        elif 'SP FP' and 'SIMD'   in comp_mem_list[i]: spfp_vector_indices.append(i)
        elif 'SP FP' and 'SCALAR' in comp_mem_list[i]: spfp_scalar_indices.append(i)
        elif 'SP FP'              in comp_mem_list[i]: spfp_others_indices.append(i)
        elif 'INT'   and 'SIMD'   in comp_mem_list[i]: int_vector_indices.append(i)
        elif 'INT'   and 'SCALAR' in comp_mem_list[i]: int_scalar_indices.append(i)
        elif 'INT'                in comp_mem_list[i]: int_others_indices.append(i)
        else:                                          others_indices.append(i)
    for i in dpfp_vector_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in dpfp_scalar_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in dpfp_others_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in spfp_vector_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in spfp_scalar_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in spfp_others_indices: ordered_comp_mem_list.append(comp_mem_list[i])
    for i in int_vector_indices:  ordered_comp_mem_list.append(comp_mem_list[i])
    for i in int_scalar_indices:  ordered_comp_mem_list.append(comp_mem_list[i])
    for i in int_others_indices:  ordered_comp_mem_list.append(comp_mem_list[i])
    for i in others_indices:      ordered_comp_mem_list.append(comp_mem_list[i])
        
    # sort Others list by data type and SIMD/scalar
    dpfp_vector_indices = []
    dpfp_scalar_indices = []
    dpfp_others_indices = []
    spfp_vector_indices = []
    spfp_scalar_indices = []
    spfp_others_indices = []
    int_vector_indices = []
    int_scalar_indices = []
    int_others_indices = []
    others_indices = []
    for i in range(len(others_list)):
        if   'DP FP' and 'SIMD'   in others_list[i]: dpfp_vector_indices.append(i)
        elif 'DP FP' and 'SCALAR' in others_list[i]: dpfp_scalar_indices.append(i)
        elif 'DP FP'              in others_list[i]: dpfp_others_indices.append(i)
        elif 'SP FP' and 'SIMD'   in others_list[i]: spfp_vector_indices.append(i)
        elif 'SP FP' and 'SCALAR' in others_list[i]: spfp_scalar_indices.append(i)
        elif 'SP FP'              in others_list[i]: spfp_others_indices.append(i)
        elif 'INT'   and 'SIMD'   in others_list[i]: int_vector_indices.append(i)
        elif 'INT'   and 'SCALAR' in others_list[i]: int_scalar_indices.append(i)
        elif 'INT'                in others_list[i]: int_others_indices.append(i)
        else:                                        others_indices.append(i)
    for i in dpfp_vector_indices: ordered_others_list.append(others_list[i])
    for i in dpfp_scalar_indices: ordered_others_list.append(others_list[i])
    for i in dpfp_others_indices: ordered_others_list.append(others_list[i])
    for i in spfp_vector_indices: ordered_others_list.append(others_list[i])
    for i in spfp_scalar_indices: ordered_others_list.append(others_list[i])
    for i in spfp_others_indices: ordered_others_list.append(others_list[i])
    for i in int_vector_indices:  ordered_others_list.append(others_list[i])
    for i in int_scalar_indices:  ordered_others_list.append(others_list[i])
    for i in int_others_indices:  ordered_others_list.append(others_list[i])
    for i in others_indices:      ordered_others_list.append(others_list[i])
        
    
    
    
    # swap columns
    temp = []
    for i in ordered_comp_list:
        words = i.split('\t')
        temp.append(words[0] + '\t' + words[4] + '\t' + words[3] + '\t' + words[2] + '\t' + words[1])
    ordered_comp_list = temp.copy()
    temp = []
    for i in ordered_mem_list:
        words = i.split('\t')
        temp.append(words[0] + '\t' + words[4] + '\t' + words[3] + '\t' + words[2] + '\t' + words[1])
    ordered_mem_list = temp.copy()
    temp = []
    for i in ordered_comp_mem_list:
        words = i.split('\t')
        temp.append(words[0] + '\t' + words[4] + '\t' + words[3] + '\t' + words[2] + '\t' + words[1])
    ordered_comp_mem_list = temp.copy()
    temp = []
    for i in ordered_comp_mem_list:
        words = i.split('\t')
        temp.append(words[0] + '\t' + words[4] + '\t' + words[3] + '\t' + words[2] + '\t' + words[1])
    ordered_comp_mem_list = temp.copy()
    temp = []
    for i in ordered_others_list:
        words = i.split('\t')
        temp.append(words[0] + '\t' + words[4] + '\t' + words[3] + '\t' + words[2] + '\t' + words[1])
    ordered_others_list = temp.copy()
    
    
    # count instructions
    comp_dict = {}
    ordered_comp_keys = []
    mem_dict = {}
    ordered_mem_keys = []
    comp_mem_dict = {}
    ordered_comp_mem_keys = []
    others_dict = {}
    ordered_others_keys = []
    for i in ordered_comp_list:
        if i in comp_dict:
            comp_dict[i] += 1
        else:
            comp_dict[i] = 1
            ordered_comp_keys.append(i)
    for i in ordered_mem_list:
        if i in mem_dict:
            mem_dict[i] += 1
        else:
            mem_dict[i] = 1
            ordered_mem_keys.append(i)
    for i in ordered_comp_mem_list:
        if i in comp_mem_dict:
            comp_mem_dict[i] += 1
        else:
            comp_mem_dict[i] = 1
            ordered_comp_mem_keys.append(i)
    for i in ordered_others_list:
        if i in others_dict:
            others_dict[i] += 1
        else:
            others_dict[i] = 1
            ordered_others_keys.append(i)
    
    
    # dump to file
    with open('ordered_opcodes.txt', 'w') as f:
        for key in ordered_comp_keys:     print(key + '\t' + str(comp_dict[key]),     file=f)
        for key in ordered_mem_keys:      print(key + '\t' + str(mem_dict[key]),      file=f)
        for key in ordered_comp_mem_keys: print(key + '\t' + str(comp_mem_dict[key]), file=f)
        for key in ordered_others_keys:   print(key + '\t' + str(others_dict[key]),   file=f)
    
    # DEBUG
    with open('ordered_ocodes_d.txt', 'w') as f:
        print('\n'.join(ordered_comp_list), file=f)
        print('\n'.join(ordered_mem_list), file=f)
        print('\n'.join(ordered_comp_mem_list), file=f)
        print('\n'.join(ordered_others_list), file=f)
        
    
    
    
def main():
    sort_instructions()

if __name__ == "__main__":
    main()