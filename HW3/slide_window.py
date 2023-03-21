import itertools as iTools
def slide_window_fn(input,width,increment):
    '''Slide Window function computes the sliding window of a list with a 
    given increment number and window width.
    :input param: Type List
    :width param: Type int
    :increment param: Type int
    :output param: Return param of type list
    '''
    assert type(input)==list and increment >0 and width>0,'input args are wrong'
    assert bool(input),'list is empty'
    return [list(iTools.islice(input,start,start+width,1)) for start in range(0,len(input),increment) if (len(input)-start>=width) ]
    