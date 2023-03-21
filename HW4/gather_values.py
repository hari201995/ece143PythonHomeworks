import random
import collections as cTools

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

def map_bitstring(x,repeatReqd):
    ''' takes a list of bitstrings (i.e., 0101)
    and maps each bitstring to 0 if the number of 
    0s in the bitstring strictly exceeds the number of 1s
    :x param: input list
    :output param: output dictionary
    '''
    assert type(x)==list and x!=None,"argument error"
    output ={}
    for i in range(len(x)):
        elem = x[i]
        acc = 0
        for k in range(len(elem)):
            acc = acc + int(elem[k])
        if len(elem)-acc>acc:
            output[elem]=[0]*repeatReqd[elem]
        else:
           output[elem]=[1]*repeatReqd[elem]
    print(output)
    return output

def gather_values(x):
    '''Generate a new dictionary with bitstrings as 
    keys and with values as lists that contain the 
    corresponding mapped values from map_bitstring
    :x param: input value
    :output param: returns a dictionary
    '''
    assert type(x)==list and x!=None,"argument error"
    output ={}

    repeatReqd = cTools.Counter(x)
    for i in range(len(x)):
        elem = x[i]
        acc = 0
        for k in range(len(elem)):
            acc = acc + int(elem[k])
        if len(elem)-acc>acc:
            output[elem]=[0]*repeatReqd[elem]
        else:
           output[elem]=[1]*repeatReqd[elem]
    print(output)

if __name__=='__main__':
    samples = get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
    gatherOutput= gather_values(samples)