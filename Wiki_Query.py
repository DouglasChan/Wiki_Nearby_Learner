import wikipedia
import time

def find_landmarks(coordinates_list):
    landmarks_list = []
    for i in range(len(coordinates_list)):
        for j in range(len(coordinates_list[i])):
            landmarks_list.append(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1]))
              
    landmarks_aggregate_list = list(set([item for sublist in landmarks_list for item in sublist])) 
    
    '''
    In its current form, landmarks_list should be a list of lists...
    
    * Could consider adding a timestamp as the first object?
    '''
    
    text_list = []
    
    for i in range(len(landmarks_aggregate_list)):
        print(wikipedia.page(landmarks_aggregate_list[i]).content)
        print(type(wikipedia.page(landmarks_aggregate_list[i]).content))
        print(len(wikipedia.page(landmarks_aggregate_list[i]).content))
        
        text_list.append(wikipedia.page(landmarks_aggregate_list[i]).content)
        
    print(text_list)
    
    return text_list
    

    
    
        #print(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1]))
        #print(type(wikipedia.geosearch(coordinates_list[i][0],coordinates_list[i][1])))
        
