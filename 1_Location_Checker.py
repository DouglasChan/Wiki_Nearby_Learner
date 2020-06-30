import requests
import time

def display_ip():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})

if __name__ == '__main__':
    counter = 0
    while True:
        display_ip()
        print(counter)
        time.sleep(0.5)
        counter += 1
    #display_ip()

#Ref