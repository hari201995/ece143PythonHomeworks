import numpy as np
import math
def find_convex_cover(pvertices,clist):
    '''Given a irregular, closed, convex polygon P with n−1 sides 
    and m circle-centers {(xi,yi)}mi contained within that polygon, 
    compute the radii, 0≤ri, of m circles centered at those m points 
    such that the sum of the areas of the circles is minimized (approximately)
    and that any vertex in P is also contained in at least one of the m circles. 
    '''
    assert isinstance(pvertices,np.ndarray),'wrong input'
    assert isinstance(clist,list),'wrong input'
    radius = [0]*len(clist)
    k=0
    for v in pvertices:
        Dist = np.linalg.norm(v-np.array(clist),axis=1)
        lowestDisCentreInd = Dist.argmin()
        lowestDisVal = Dist[lowestDisCentreInd]
        if radius[lowestDisCentreInd] < lowestDisVal:
            radius[lowestDisCentreInd]=lowestDisVal
    return radius


if __name__=='__main__':
    pvertices = np.array([[ 0.573,  0.797],           
                        [ 0.688,  0.402],                                                              
                        [ 0.747,  0.238],                                                              
                        [ 0.802,  0.426],                                                              
                        [ 0.757,  0.796],                                                              
                        [ 0.589,  0.811]])                                                             
                                                                                                       
    clist = [(0.7490863467660889, 0.4917635308023209),                                       
              (0.6814339441396109, 0.6199470305156477),                                                
              (0.7241617773773865, 0.6982813914515696),                                                
              (0.6600700275207232, 0.7516911829987891),                                                
              (0.6315848053622062, 0.7730550996176769),                                                
              (0.7348437356868305, 0.41342916986639894),                                               
              (0.7597683050755328, 0.31729154508140384)]  
    print(find_convex_cover(pvertices,clist))