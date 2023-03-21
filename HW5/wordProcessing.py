from urllib.request import urlopen
from collections import Counter 

def get_average_word_length(words):
    ''' Average length of words in list
    :word param: list
    '''
    assert bool(words),'wrong input'
    lenWords = [len(elem) for elem in words]
    avgLen = sum(lenWords)/len(lenWords)
    return avgLen

def get_longest_word(words):
    ''' longest length of words in list
    :word param: list
    '''
    assert bool(words),'wrong input'
    sortedWord = sorted(words,key=len)
    return sortedWord[-1]

def get_longest_words_startswith(words,start):
    ''' longest length of words in list with a letter
    :word param: list
    '''
    assert bool(words) and type(start)==str,'wrong input'
    filteredList = [elem for elem in words if elem.startswith(start)]
    return get_longest_word(filteredList)

def get_most_common_start(words):
    ''' common starting char of words in list
    :word param: list
    '''
    assert bool(words),'wrong input'
    firstChar = [elem[0] for elem in words]
    charDict = Counter(firstChar)
    return max(charDict, key = charDict.get)

def get_most_common_end(words):
    ''' common ending char of words in list
    :word param: list
    '''
    assert bool(words),'wrong input'
    lastChar = [elem[-1] for elem in words]
    charDict = Counter(lastChar)
    return max(charDict, key = charDict.get)

if __name__ =='__main__':
    u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
    response = urlopen(u)
    words = [i.strip().decode('utf8') for i in response.readlines()]
    print(get_average_word_length(words))
    print(get_longest_word(words))
    print(get_longest_words_startswith(words,'a'))
    print(get_most_common_start(words))
    print(get_most_common_end(words))
                                       