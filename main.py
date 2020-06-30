import wikipedia
import time
import Location_Checker
import Wiki_Query
import NLP_Processing_Landmarks

if __name__ == '__main__':
    coordinates_list = Location_Checker.display_ip()
    text_list = Wiki_Query.find_landmarks(coordinates_list)
    NLP_Processing_Landmarks.processing_pages(text_list)

print('Finished.')

time.sleep(15)