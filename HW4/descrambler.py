import itertools as iTools
from collections import Counter
def descrambler(input,separationTuple):
    '''You are given a sequence of n lower-case letters and a k-tuple
    of integers that indicate partition-lengths of the sequence. Also, 
    you have a dictionary of commonly used words. The n letters represent 
    a phrase of k words where the length of the jth word is the jth element 
    of the tuple.
    :input param:input list
    :separationTuple param: Input tuple
    :output param: return iterator
    '''
    assert bool(input) and type(input)==str,'wrong input strings'
    assert bool(separationTuple),'empty tuple'

    # Reading the file
    fid = open(r"C:\Hari\Q5_books\143\HW4\google-10000-english-no-swears.txt",'r')
    words = fid.read()
    words = words.splitlines()
    
    # Creating the dictionary
    wordDict ={}
    for kId in separationTuple:
        filteredDict = [elem for elem in words if len(elem)==kId]
        tmp=[]
        for i in range(len(filteredDict)):
            freq1, freq2 = Counter(filteredDict[i]), Counter(input)
            if(all(freq1[ind] <= freq2[ind] for ind in filteredDict[i])):
                tmp.append(filteredDict[i])
        if kId in wordDict.keys():
            key = kId+max(separationTuple)
        else:
            key = kId
        wordDict[key]=tmp

    combos = iTools.product(*(wordDict.values()))
    for elem in combos:
        string = ''.join(elem)
        if sorted(string)==sorted(input):
            output = ' '.join(elem)
            yield output

if __name__=='__main__':
    print(list(descrambler('hellothere',(6,8))))

