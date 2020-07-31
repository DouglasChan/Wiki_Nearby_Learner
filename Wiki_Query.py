import wikipedia
import time

def find_landmarks(coordinates_list):
    landmarks_list = []
    for i in range(len(coordinates_list)): #For all the coordinates
        landmarks_list.append(wikipedia.geosearch(coordinates_list[i][0][1],coordinates_list[i][1][1],radius=1000)) #1 km radius by default.
        print(landmarks_list[len(landmarks_list)-1]) #Most recent addition to the landmarks list

    landmarks_aggregate_list = list(set([item for sublist in landmarks_list for item in sublist])) #Using set will find only unique values of landmarks
    
    '''
    In its current form, landmarks_list should be a list of lists...
    
    '''
    
    text_list = []
    
    for i in range(len(landmarks_aggregate_list)):
        print(wikipedia.page(landmarks_aggregate_list[i]).content)
        print(len(wikipedia.page(landmarks_aggregate_list[i]).content))
        
        text_list.append(wikipedia.page(landmarks_aggregate_list[i]).content)
    
    return text_list