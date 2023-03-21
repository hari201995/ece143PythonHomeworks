import numpy as np
import itertools as iTools 
import random
def solvefrob(coefs,b):
    ''' The Frobenius equation is the Diophantine equation,a_1 x_1 +... + a_n x_n = b
    where a_i> 0 are positive integers, b> 0 is a positive integer, and the solution x_i
    consists of non-negative integers
    :coefs param: List of coefs [a1,a2,....,an]
    :b param: RHS of diaphantine eqn
    '''
    assert bool(coefs) and not(any(x<=0 for x in coefs)),'empty list'
    assert type(b)==int and b>0,'wrong b value'

    bcArray = np.broadcast(b,coefs)
    maxLimits = [np.floor(elem[0]/elem[1]).astype('int') for elem in bcArray]
    solnDict = {random.uniform(0,max(maxLimits)) : np.linspace(start=0,stop=key,num=key+1,dtype='int') for key in maxLimits}
    sampleSpace =tuple(iTools.product(*solnDict.values()))
    allCombos = np.sum(np.array(coefs) * np.array(sampleSpace),axis=1).astype('int')
    solnInd = np.flatnonzero(allCombos==b)
    output = [sampleSpace[ind] for ind in solnInd]
    return output

if __name__=='__main__':
    print(solvefrob([1,1],10))

