def next_permutation(t:tuple)->tuple:
    '''Given a permutation of any length, generate the
    next permutation in lexicographic order. For example, 
    this are the permutations for [1,2,3] in lexicographic order
    '''
    assert isinstance(t,tuple),'wrong input'
    assert t!=[],'empty'
    for i in t:
        if i<0:
            assert 0,'negative ip'
    assert len(t) == len(set(t)),'duplicate'
    t = list(t)
    pivotInd=0
    for i in range(len(t)-1,0,-1):
        if t[i] < t[i-1]:
            continue
        else:
            pivotInd = i-1
            break
    suffix = t[pivotInd+1:]
    diff = [elm-t[pivotInd] for elm in suffix]
    allNegFlag=0
    for elm in diff:
        if elm<0:
            allNegFlag=1
        else:
            allNegFlag=0
    if allNegFlag==0:
        minInd = diff.index(min(diff))
    else:
        return tuple(t[::-1])
    swapInd = (pivotInd) + minInd +1
    temp = t[swapInd]
    t[swapInd] = t[pivotInd]
    t[pivotInd] = temp
    t[pivotInd+1:] = t[pivotInd+1:][::-1]
    return tuple(t)

if __name__=='__main__':
    print(next_permutation((1,3,2)))