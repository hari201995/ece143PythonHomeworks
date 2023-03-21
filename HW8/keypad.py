import networkx as nx

def get_all_paths(a,b):
    '''With the usual 9-digit keypad, starting at any digit, draw a continuous unbroken path 
    to any other digit, how many such paths are possible between any two digits, excluding 
    repeated digits?
    '''
    assert a<=9 and a>=1,'wrong a'
    assert b<=9 and b>=1,'wrong b'
    assert a!=b, 'wrong input'

    # create a graph
    G = nx.Graph()

    # add nodes
    for i in range(1,10,1):
        G.add_node(i)
    
    # add edge
    G.add_edge(1,2)
    G.add_edge(2,1)
    G.add_edge(1,4)
    G.add_edge(4,1)
    G.add_edge(1,5)
    G.add_edge(5,1)
    G.add_edge(2,3)
    G.add_edge(3,2)
    G.add_edge(2,5)
    G.add_edge(5,2)
    G.add_edge(2,6)
    G.add_edge(6,2)
    G.add_edge(2,4)
    G.add_edge(4,2)
    G.add_edge(3,5)
    G.add_edge(5,3)
    G.add_edge(3,6)
    G.add_edge(6,3)
    G.add_edge(4,5)
    G.add_edge(5,4)
    G.add_edge(5,6)
    G.add_edge(6,5)
    G.add_edge(4,7)
    G.add_edge(7,4)
    G.add_edge(7,8)
    G.add_edge(8,7)
    G.add_edge(5,8)
    G.add_edge(8,5)
    G.add_edge(7,5)
    G.add_edge(5,7)
    G.add_edge(4,8)
    G.add_edge(8,4)
    G.add_edge(8,9)
    G.add_edge(9,8)
    G.add_edge(6,9)
    G.add_edge(9,6)
    G.add_edge(5,9)
    G.add_edge(9,5)

    paths = list(nx.all_simple_paths(G, source=a, target=b))
    return paths

def get_estimated_completion_prob(x):
    '''A partial sequence for a pattern lock is retrieved, x = [2,6,9]. Assuming all paths are
    equally likely, estimate the probability of each of the valid paths that start with x
    '''
    assert isinstance(x,list),'wrong input'

    head = list(range(1,10,1))
    tail =  list(set(head) ^ set(x))
    result={}
    lenSampleSpace=0
    for ends in tail:
        allPaths = get_all_paths(x[0],ends)
        reqdPath = [path for path in allPaths if path[:len(x)]==x]
        result[ends] = len(reqdPath)
        lenSampleSpace += len(reqdPath)
    for key,value in result.items():
        result[key] = value/lenSampleSpace
    return result

                 

if __name__=='__main__':
    print(get_estimated_completion_prob([2,6,9]))