import random
import collections as cTools
from collections import Counter

def gather_values(x):
    '''Generate a new dictionary with bitstrings as 
    keys and with values as lists that contain the 
    corresponding mapped values from map_bitstring
    :x param: input value
    :output param: returns a dictionary
    '''
    assert type(x)==list and x!=[],"argument error"
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
    return (output)


def threshold_values(seq,threshold=1):
    '''Threshold those values based upon their frequency and value
    :seq param: Dictionary
    :threshold param: Input threshold
    :onesThatPass paaram: Return dictionary
    '''
    assert bool(seq),'Empty list'
    seq = gather_values(seq)
    dupe={}
    for keys in seq.keys():
        if type(seq[keys])==int:
            seq[keys]=[(seq[keys])]
        if 0 not in seq[keys]:
            dupe[keys]=len(seq[keys])
        else: 
            dupe[keys]=0
    onesThatPass = sorted(dupe.items(), key=lambda x:(-1*x[1],x[0]))
    onesThatPass = dict(onesThatPass)
    flag=1
    for keys in onesThatPass.keys():
        if flag<=threshold:
            onesThatPass[keys]=1
            flag+=1
        else:
            onesThatPass[keys]=0 
    return onesThatPass


if __name__ =='__main__':
    seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001'] 
    out = threshold_values(seq,threshold=3)
    print(out)
