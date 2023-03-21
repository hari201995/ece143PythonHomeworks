def get_trapped_water(seq):
    '''how many units of water remain trapped between
    the walls in the map.
    '''
    assert isinstance(seq,list),'wrong input'
    assert seq !=[],'wrong input'
    for i in seq:
        if i<0:
            assert 0,'Wrong input'
        if type(i) != int:
            assert 0,'Wrong input'
    waterTrapped =0
    for ind in range(1,len(seq)-1):
        left = seq[:ind]
        right = seq[(ind)+1:]
        waterlevel = min(max(left),max(right))
        if seq[ind] > waterlevel:
            continue
        waterTrapped += waterlevel - seq[ind]
    return waterTrapped

if __name__ =='__main__':
    print(get_trapped_water([3,0,1,3,0,5,3,2]))
        
    