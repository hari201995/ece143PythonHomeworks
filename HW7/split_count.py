import pandas as pd
import itertools
import collections

def split_count(x):
    '''x is a pd.Series object and 
    it returns a pd.DataFrame object
    '''
    assert isinstance(x,pd.Series),"wrong data"
    extractedOp = x
    c = extractedOp.str.split(',')

    s_flat = c.apply(pd.Series).stack().tolist()
    listWoSpace = [s.lstrip() for s in s_flat]
    result = dict(collections.Counter(listWoSpace))
    df = pd.DataFrame(list(result.items()), columns=['Name','count'])
    df.set_index('Name', inplace=True)
    df.index.name = None
    return df

def add_month_yr(x):
    