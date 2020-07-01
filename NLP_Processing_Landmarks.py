import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import time
from nltk.tree import Tree

def processing_pages(text_list):
    ne_master = []

    for i in range(len(text_list)): #text_list contains all the text articles of identified landmarks.
        ne_single_page = []
        
        custom_sent_tokenizer = PunktSentenceTokenizer() #Trained vs not? Leaving as default
        
        tokenized = custom_sent_tokenizer.tokenize(text_list[i]) #Attempt at tokenizing each sentence within Wikipedia page. Potential problems with new lines & content
        
        
        for sentence in tokenized:
            words = nltk.word_tokenize(sentence) #Unigram tokenized words. Sometimes has problems parsing sentences with addresses. 
            
            tagged = nltk.pos_tag(words) #Pretty much the same list as earlier, but with each word as a tuple now with POS as second part of tuple.
            
            namedEnt = nltk.ne_chunk(tagged) #NLTK tree object
            
            #test_list = [word for word,pos in namedEnt.pos() if pos=='NNP']
            
            ne_in_sent = []
            for subtree in namedEnt: #Tuple? or tree type if there's a named entity in it?
            
                if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
                    ne_label = subtree.label() #String type, it's the prefix before the named entity
                    
                    ne_string = " ".join([token for token, pos in subtree.leaves()]) #String, name of the named entity?
                    
                    ne_in_sent.append((ne_string, ne_label)) #List of named entities, and the NE type?
                    
                    #print(ne_in_sent)
                    time.sleep(2)
                    
                    #print(ne_in_sent)
                    #print(len(namedEnt))
                    
                    if subtree == namedEnt[len(namedEnt)-1]:
                        print('yup.')
                        time.sleep(2)
            
            print(ne_single_page)
            ne_single_page.append(ne_in_sent)
            #print(ne_master)
            
        ne_master.append(ne_single_page)
    print(ne_master)
            
            #Phrase tokenize?
        
            #time.sleep(0.1)
            #print(item)
            #print(len(tokenized))
        
        #print(tokenized)
        #for j in tokenized:
        #    print(j)
    
        #tokens = nltk.word_tokenize(text_list[i])
        
        #print("Parts Of Speech: ", nltk.pos_tag(tokens))
        
#if __name__ == '__main__':
    