import random

def get_sample(nbits=3,prob=None,n=1):
    '''The function chooses random sample from a dictionary based 
    on a probability
    :nbits param: Input number of bits
    :prob param: Dictionary with pmf
    :n param: Output length
    :output param: returns the list of selected numbers
    '''
    assert sum(list(prob.values()))==1, "wrong probability vector"
    assert type(nbits)==int and type(n)==int, 'wrong input type'
    assert len(prob)>0, 'empty dictionary'
    output = random.choices(population = list(prob.keys()),weights = list(prob.values()),k=n)
    return output

