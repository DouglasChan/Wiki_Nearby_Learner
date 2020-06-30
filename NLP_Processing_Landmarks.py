import nltk

def processing_pages(text_list):
    for i in range(len(text_list)):
        tokens = nltk.word_tokenize(text_list[i])
        
        print("Parts Of Speech: ", nltk.pos_tag(tokens))