import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import time

def processing_pages(text_list):
    for i in range(len(text_list)):
    
        custom_sent_tokenizer = PunktSentenceTokenizer() #Trained vs not? Leaving as default
        
        tokenized = custom_sent_tokenizer.tokenize(text_list[i])
        
        #for item in tokenized:
        #    print(item)
        
        for item in tokenized:
            time.sleep(0.1)
            print(item)
            print(len(tokenized))
        
        #print(tokenized)
        #for j in tokenized:
        #    print(j)
    
        #tokens = nltk.word_tokenize(text_list[i])
        
        #print("Parts Of Speech: ", nltk.pos_tag(tokens))
        
#if __name__ == '__main__':
    