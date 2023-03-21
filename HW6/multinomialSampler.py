import random

def multinomial_sample(n,p,k=1):
    '''                                                                 
    Return samples from a multinomial distribution.                                                                                          
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert type(n)==int and type(k)==int,'wrong input type'
    assert type(p)==list and p!=[],'empty list'
    listOfSamples =[]
    for i in range(k):
        trial=[]
        for l in range(len(p)):
            trial.append(0)
        for j in range(n):
            outcome =random.choices(range(len(p)), p,k=1)
            trial[outcome[0]] = trial[outcome[0]]+1
        listOfSamples.append(trial)
    return listOfSamples

if __name__=='__main__':
    print(multinomial_sample(10,[0.3,0.3,0.4],10))