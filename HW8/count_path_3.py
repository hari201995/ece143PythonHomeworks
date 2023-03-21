def get_all_paths(curr_row,curr_col,m,n,blocks):
    ''' get all paths starting from a given (r,c) given the obstacle matrix 
    '''
    assert type(curr_row) and type(curr_col) and type(m) and type(n) is int 
    assert type(blocks) is list

    if curr_row==m or curr_col==n or (curr_row,curr_col) in blocks: 
        return 0
    elif (curr_row, curr_col) == (m-1,n-1): 
        return 1
    else: 
        path_right = get_all_paths(curr_row+1,curr_col,m,n,blocks) 
        path_down = get_all_paths(curr_row,curr_col+1,m,n,blocks)
        return path_right + path_down

def count_paths(m,n,blocks):
    '''A two dimensional grid has M horizontal rows and N vertical columns. 
    Let (i,j) denote the square at the (i+1)th row from the top and the 
    (j+1)th column from the left i.e., they are 0-indexed'''
    assert isinstance(m,int) and isinstance(n,int),'wrong input'
    for blk in blocks:
        if blk[0]>m:
            assert 0,'wrong input'
        if blk[1]>n:
            assert 0,'wrong input'
        if blk[0] <0 or blk[1]<0:
            assert 0,'wrong input'

    if m==1 and n==1:
        return 0
    
    total_paths = get_all_paths(0,0,m,n,blocks)
    return total_paths
    
if __name__ == '__main__':
    print(count_paths(3,4,[(0,3),(1,1)]))