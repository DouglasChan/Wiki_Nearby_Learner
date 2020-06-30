import wikipedia
import time

def find_landmarks(coordinates_list):
    landmarks_list = []
    for i in range(len(coordinates_list)):
        for j in range(len(coordinates_list[i])):
            landmarks_list.append(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1]))
            
    print(landmarks_list)
        #print(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1]))
        #print(type(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1])))
        
