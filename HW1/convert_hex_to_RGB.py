def convert_hex_to_RGB(instring):
    
    """Convert Hex values to RGB values
    :param instring: Input strings
    :type: List
    :Return rgbList : RGB tuples corresponding to i/p strings
    :type: List of tuples
    """
    assert instring!=[],"instring is null"
    rgbList =[]
    for i in range(len(instring)):
        hexStr = instring[i][1:]
        assert len(hexStr)==6,"minimum length reqd is 6"
        tupleInt =()
        intArr=[]
        intArr.append(int(hexStr[0:2],16))
        intArr.append(int(hexStr[2:4],16))
        intArr.append(int(hexStr[4:6],16))
        tupleInt = (intArr[0],intArr[1],intArr[2])
        rgbList.append(tupleInt)
    return rgbList