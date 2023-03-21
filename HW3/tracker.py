from time import sleep
import random
from datetime import datetime
import itertools as it

 
def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime


def tracker(p,limit):
    ''' function to count the secs after calling a function
    :p param: input of generator type
    :limit param: trackng limit
    '''
    assert type(limit) is int,'asserting due to wrong limit value'
    assert bool(p), 'assert due to incorrect args'
    silo = None
    count = 0
    flag=1
    while True:    
        secs = next(p).seconds
        if count == limit:
            break
        if(secs %2  == 1):
            count +=1
        silo = yield count
        if silo != None:
            limit = silo
