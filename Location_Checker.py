import requests
import time
import csv
from os import getcwd, listdir
\

def find_csv_filenames(path_to_dir, suffix = '.csv'):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

def display_ip():

    coordinates_list = []
    
    path = getcwd() # Current working directory
    
    filenames = find_csv_filenames(path)
    for name in filenames:
        print(name)
    
    #Reading in CSV data
    
    #Take given csv file
    #Ideally later would want all csv files combined
    
    #Output list of latitudes and longiudes
    
    
    #counter = 0
    
    
    
    #while counter < 1000000:

        # Code below isn't great -- since takes the geolocation of the cell tower and not anything actually useful. 

        #ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        #my_ip = ip_request.json()['ip']
        #geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        #geo_data = geo_request.json()
        #print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})
        #coordinates_list.append(tuple((geo_data['latitude'],geo_data['longitude'])))
        
    #    counter += 1
    #    print(counter)
    #    time.sleep(15)
    
    print(coordinates_list)
    return coordinates_list

if __name__ == '__main__':
    display_ip()


#Ref
#1. https://note.nkmk.me/en/python-os-getcwd-chdir/#:~:text=Get%20the%20current%20working%20direcory%3A%20os.,-getcwd()&text=getcwd()-,os.,the%20result%20with%20print()%20.&text=getcwd%20stands%20for%20%22get%20current%20working%20directory%22.