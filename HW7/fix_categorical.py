import pandas as pd
import collections

def add_month_yr(x):
    ''' take in the x survey dataframe and then output the 
    same dataframe with a new month-yr column
    '''
    assert isinstance(x,pd.DataFrame),'wrong input'
    data = x
    timeStamp = data['Timestamp']
    dateOnly = pd.to_datetime(timeStamp).dt.date
    dateOnly = dateOnly.apply(lambda x: x.strftime('%b-%Y'))
    data['month-yr'] = dateOnly
    data['month-yr']=data['month-yr'].astype(str)
    return data


def fix_categorical(x):
    ''' count_month_yr to create the following 
    dataframe using your new column month-yr
    '''
    assert isinstance(x,pd.DataFrame),'wrong input'   
    data = x
    extractedData = data['month-yr'].to_list()
    dateList = list(collections.Counter(extractedData))
    catDataType = pd.CategoricalDtype(categories=dateList, ordered=True)
    data['month-yr'] = data['month-yr'].astype(catDataType)
    return data