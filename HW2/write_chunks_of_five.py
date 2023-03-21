import itertools as iTools

def write_chunks_of_five(words,fname):
    '''write_chunks_of_five creates a file that has 5 mon-overlapping sequence from
    the input words and stores it in a file named fname.
    :words param: List of words that will be grouped
    :fname param: Name of the output file 
    '''
    # Asserts
    assert bool(words) and all(isinstance(element,str) for element in words),'words dictionary is either empty or it has a non string element'
    assert fname != None and type(fname)==str,'file name is bad or not present'

    # Functionality
    numConsecWords = 5
    words = iter(words)
    listOfWords = iter(lambda: list(iTools.islice(words, numConsecWords)),())
    
    # writing list of words into the file
    fid = open(fname,'w')
    for consecWords in listOfWords:
        if bool(consecWords):
            fid.write(' '.join(consecWords))
            fid.write('\n')
        else:
            break
    fid.close()

