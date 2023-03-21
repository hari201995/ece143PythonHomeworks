def compute_sum_to_n(input):
    """ Function to compute the sum until n numbers
    :param input: integer
    :return acc: returns the sum until n
    :type: integer
    """    
    #function validation
    assert not(input is None),"input is Null"
    assert type(input)==int,"Input is not integer"
    assert input>=0,"input is negative"
    #functionality
    acc=0
    for i in range(input+1):
        acc = acc + i
    return acc

    