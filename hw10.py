import random
def bigram_count(text):
    '''
    Purpose:
        Takes a string and creates a dictionary of all bigrams in the string
    Input Parameters:
        text = a string of text
    Return Value:
        a dictionary representing the bigrams in the provided string
    '''
    bigram = {}
    words = text.split()
    for i, value in enumerate(words):
        if i != (len(words)-1):
            bigram[value] = bigram.get(value,[]) + [words[i+1]]
    return bigram

def random_sentence(bigram, start, length):
    '''
    Purpose:
        Creates a random sentence from the provided bigram dictionary, given the
        starting word and amount of words to output in the sentence
    Input Parameters:
        bigram = a dictionary of bigrams
        start = a string representing the starting word
        length = a int representing the amount of words in the output sentence
    Return Value:
        a string representing a random sentence of the given length
    '''
    sentence = []
    sentence.append(start)
    x = 0
    while len(sentence) != length:
        if sentence[x] not in bigram.keys():
            sentence.append(start)
        else:
            sentence.append(random.choice(bigram[sentence[x]]))
        x += 1
    return ' '.join(sentence)

def rand_sent_file(fname, length):
    '''
    Purpose:
        Creates a random sentence of the given length whose data is drawn from
        the given text file.
    Input Parameters:
        fname = a string representing the name of the file
        length = a int representing the amount of words in the output sentence
    Return Value:
        a string representing a random sentence of the given length
    '''
    with open(fname, 'r') as f:
        text = f.read()
        bigram = bigram_count(text)
    return random_sentence(bigram, random.choice(list(bigram.keys())), length)
