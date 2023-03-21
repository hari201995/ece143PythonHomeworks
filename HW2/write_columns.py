def  write_columns_fn(data,fname):
    ''' function write_columns takes the elements of data and creates
    (dataValue,dataValue**2,(dataValue+dataValue**2)/3) rows which are 
    written in columns in the fname file.
    :data param: list of dataValues
    :fname param: string containing the name of the csv file
    '''
    #Asserts
    assert isinstance(data,list)==1 and bool(data),"data is not a list or data is empty"
    assert fname!=None and type(fname)==str,"No fname given or the fname is not string"
    assert all(isinstance(x, int) for x in data) or all(isinstance(x, float) for x in data),"List contains element which is not an integer / Float"
    
    #Functionality
    secondColumn = [round(dataVal**2,2) for dataVal in data]
    thirdColumn = [round((dataVal + secondColumnVal)/3,2) for dataVal,secondColumnVal in zip(data,secondColumn)]
    concatedColumns = zip(data,secondColumn,thirdColumn)

    
    #Writing into file
    fid = open(fname,'w')
    for itr in concatedColumns:
        fid.write(",".join(map(str,itr)) + "\n")
    fid.close()
    
        
