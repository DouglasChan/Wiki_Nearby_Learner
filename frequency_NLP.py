import time
from itertools import groupby

def frequency_counter(ne_master):
    for i in range(len(ne_master)):
        frequency_list = [len(list(group)) for key, group in groupby(ne_master[i])]
        key_list = [key for key,group in groupby(ne_master[i])]
        #print(frequency_list)
        #print(key_list)
        
    #Grouped together
    
    part_flat_ne_master = [item for sublist in ne_master for item in sublist]
    
    flat_ne_master = []
    
    for i in range(len(part_flat_ne_master)):
        if len(part_flat_ne_master[i]) > 1:
            for j in range(len(part_flat_ne_master[i])):
                flat_ne_master.append(part_flat_ne_master[i][j])
        else:
            flat_ne_master.append(part_flat_ne_master[i])
    
    print(flat_ne_master)
    print(len(flat_ne_master))
    
    flat_ne_master_single_type = []
    
    for i in range(len(flat_ne_master)):
        if type(flat_ne_master[i]) == list:
            if len(flat_ne_master[i]) == 0:
                continue
            else:
                flat_ne_master_single_type.append(flat_ne_master[i][0])
        else:
            flat_ne_master_single_type.append(flat_ne_master[i])
    
    for i in range(len(flat_ne_master_single_type)):
        print(type(flat_ne_master_single_type[i]))
        
    print(flat_ne_master_single_type)
    print(type(flat_ne_master_single_type))
    
    time.sleep(1000)
    
    frequency_list = [len(list(group)) for key, group in groupby(flat_ne_master)]
    key_list = [key for key,group in groupby(flat_ne_master)]
    
    combined_list = [(frequency_list[i], key_list[i]) for i in range(0, len(frequency_list))]
    
    print(combined_list)
    #for i in range(len(frequency_list)):
    #    combined_list =
    #    for 
        
    #    print(frequency_list)
    #    print(key_list)
    #    print(len(frequency_list))
    #    print(len(key_list))