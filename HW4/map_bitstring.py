def map_bitstring(x):
    ''' takes a list of bitstrings (i.e., 0101)
    and maps each bitstring to 0 if the number of 
    0s in the bitstring strictly exceeds the number of 1s
    :x param: input list
    :output param: output dictionary
    '''
    x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
    assert type(x)==list and x!=None,"argument error"
    output ={}
    for i in range(len(x)):
        elem = x[i]
        acc = 0
        for k in range(len(elem)):
            acc = acc + int(elem[k])
        if len(elem)-acc>acc:
            output[elem]=0
        else:
            output[elem]=1
    print(output)
    return output
