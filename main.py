import wikipedia
import time
import Location_Checker
import Wiki_Query

if __name__ == '__main__':
    coordinates_list = Location_Checker.display_ip()
    Wiki_Query.find_landmarks(coordinates_list)

print('Finished.')

time.sleep(15)