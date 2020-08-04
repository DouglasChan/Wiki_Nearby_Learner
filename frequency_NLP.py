import time
from itertools import groupby
import pandas as pd

def frequency_counter(ne_master):

    for i in range(len(ne_master)):
        flat_master = [item for sublist in ne_master[i] for item in sublist]
        
        flat_master.sort()
        
        print(flat_master)
        print(len(flat_master))
        
        frequency_list = [(key, len(list(group))) for key, group in groupby(flat_master)]
        print(frequency_list)
        print(len(frequency_list))
        
        #time.sleep(1000)

        #key_list = [key for key,group in groupby(flat_master)]
        
        df = pd.DataFrame(frequency_list,columns=['tuple key','frequency'])
        
        df = df.sort_values(by=['frequency'], ascending=False)
        
        pd.set_option('display.max_rows', 500)
        
        print(df)
        #print(key_list)
        
    #Grouped together
    '''
    part_flat_ne_master = [item for sublist in ne_master for item in sublist]
    
    print(part_flat_ne_master)
    #time.sleep(1000)
    
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
    
    #time.sleep(1000)
    
    frequency_list = [len(list(group)) for key, group in groupby(flat_ne_master_single_type)]
    key_list = [key for key,group in groupby(flat_ne_master_single_type)]
    
    combined_list = [(frequency_list[i], key_list[i]) for i in range(0, len(frequency_list))]
    '''
    
    #print(frequency_list)
    #print(combined_list)
    #for i in range(len(frequency_list)):
    #    combined_list =
    #    for 
        
    #    print(frequency_list)
    #    print(key_list)
    #    print(len(frequency_list))
    #    print(len(key_list))
    
    
    [[('Chinese Martyrs Catholic Church', 'ORGANIZATION'), ('Catholic', 'ORGANIZATION'), ('Greater Toronto Area', 'ORGANIZATION'), ('Chinese', 'GSP'), ('Catholics', 'ORGANIZATION')], [('Scarborough', 'GPE'), ('Markham', 'GPE'), ('Catholic', 'ORGANIZATION'), ('Chinese', 'GPE'), ('GTA', 'ORGANIZATION')], [('Chinese Martyrs', 'ORGANIZATION'), ('Chinese', 'GPE'), ('China', 'GPE')], [('See', 'PERSON')], [('Michael', 'PERSON'), ('Cathedral', 'ORGANIZATION'), ('Toronto St', 'ORGANIZATION')], [('Paul', 'PERSON'), ('Basilica St', 'ORGANIZATION')], [('Patrick', 'PERSON'), ('Church', 'GPE'), ('Toronto', 'ORGANIZATION'), ('Lourdes Roman Catholic Church', 'PERSON'), ('Toronto', 'ORGANIZATION'), ('Chinese', 'GPE'), ('Catholic', 'ORGANIZATION'), ('Greater Toronto Area St', 'ORGANIZATION')], [('Tsao Catholic Church', 'PERSON'), ('Mount Carmel Chinese Catholic Church Saviour', 'PERSON'), ('Catholic Church', 'ORGANIZATION'), ('Chinese', 'GPE'), ('Martyrs Catholic Church', 'PERSON'), ('Wikimedia Commons', 'ORGANIZATION'), ('Chinese Martyrs Catholic', 'ORGANIZATION')]]