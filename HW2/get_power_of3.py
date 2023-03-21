import itertools as iTools
from operator import mul

def get_power_of3(input):
    '''Get the weights for the set {1,3,9,27} such that the resulting number is 
    less than 40 using +/- operation only.
    :input param: integer.
    :weights param: return list of weights.
    '''
    # Asserts
    assert input != None and type(input)==int and input>=1 and input<=40,"Invalid input number"
    
    #Function
    flag = 0
    powerOfThree = [1,3,9,27]
    operationList = [-1,0,1]
    operationCombos = iTools.product(operationList,repeat=len(powerOfThree))    
    for attempt in operationCombos:
        if sum(map(mul,attempt,powerOfThree))==input:
            flag =1
            return list(attempt)
    assert flag!=0,"The combination is not available"
    