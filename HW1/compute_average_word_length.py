def compute_average_word_length(instring,unique=False):
    """Compute_average_word_length_fn computes the number of words in a sentence
    :param instring: input string
    :type: String
    :param unique: Flag to tell if to count unique words
    :type:boolean
    :return numWords: number of unique/non-unique words
    :type: Integer
    """
    assert instring!=None and type(instring)==str ,"input is empty or type is not string"

    if unique==False:
        numWords = len(instring.split())
        return numWords
    else:
        uniqueWords = set(instring.split())
        numWords = len(uniqueWords)
        return numWords
