def fibonacci(n):
    ''' Function yields fibonacci of n numbers
    :n param: Input Number until n
    :n1 param: Output yield
    '''
    assert type(n)==int and n>=0,"wrong input"
    n1 = 1
    n2 = 1
    for i in range(n):
        n3 = n1+ n2
        yield(n1)
        n1 = n2
        n2 = n3