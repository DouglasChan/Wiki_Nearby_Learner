import requests
import time

def display_ip():

    coordinates_list = []
    
    counter = 0
    
    while counter < 20:

        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        geo_data = geo_request.json()
        print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})
        coordinates_list.append(tuple((geo_data['latitude'],geo_data['longitude'])))
        
        counter += 1
    
    print(coordinates_list)
    return coordinates_list

if __name__ == '__main__':
    display_ip()


#Ref
#