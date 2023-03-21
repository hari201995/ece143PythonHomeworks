def is_string_integer(input):
    
    """ To test if a given string is a valid base 10 number
    :param input: Input single length string
    :Type: String
    :return: True or false
    """
    assert input!=[],"input string empty"
    for i in range(10):
        if str(i)==input:
            return True
        else:
            continue
    return False
