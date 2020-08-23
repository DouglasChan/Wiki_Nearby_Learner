import wikipedia
import time
import Location_Checker
import Wiki_Query
import NLP_Processing_Landmarks
import frequency_NLP

if __name__ == '__main__':
    coordinates_list = Location_Checker.display_ip()
    text_list, number_of_articles = Wiki_Query.find_landmarks(coordinates_list)
    ne_master = NLP_Processing_Landmarks.processing_pages(text_list)
    frequency_NLP.frequency_counter(ne_master)
    
    print(number_of_articles)

print('Finished.')

time.sleep(15)