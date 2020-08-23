import requests
import time
import csv
from os import getcwd, listdir

def find_csv_filenames(path_to_dir, suffix = '.csv'):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

def displaying_all_coordinates(csv_file):

    with open(csv_file) as csvfile:
        latitude_list = []
        longitude_list = []
        time_list = []
        tuple_list = []
    
        filereader = csv.reader(csvfile)
        
        counter = 0
        
        for row in filereader: #Divides the data into 3 separate lists (overall probably less efficient)
        
            if counter % 3 == 0:
                latitude_list.append(row)
            elif counter % 3 == 1:
                longitude_list.append(row)
            elif counter % 3 == 2:
                time_list.append(row)
        
            counter += 1
        
        for i in range(len(latitude_list)): #Adds 
            tuple_list.append((latitude_list[i],longitude_list[i],time_list[i]))
               
        return tuple_list
        
def display_ip():
    
    path = getcwd() # Current working directory
    
    filenames = find_csv_filenames(path)
    
    coordinates_master_list = []
    
    for name in filenames:
        
        coordinates_list = displaying_all_coordinates(name)
        
        coordinates_master_list.append(coordinates_list)
    
    #Making list of lists into singular flat list.
    #Idea behind this is that writing to csv for every 100 measurements is fairly arbitrary. 
    coordinates_master_list = [item for sublist in coordinates_master_list for item in sublist]
    
    return coordinates_master_list

if __name__ == '__main__':
    display_ip()

#Ref
#1. https://note.nkmk.me/en/python-os-getcwd-chdir/#:~:text=Get%20the%20current%20working%20direcory%3A%20os.,-getcwd()&text=getcwd()-,os.,the%20result%20with%20print()%20.&text=getcwd%20stands%20for%20%22get%20current%20working%20directory%22.
#2. 
#https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052