from itertools import product
from collections import Counter
import itertools
import copy

def descrambler(w,k):
    """
Created on Thu Feb  3 00:13:52 2022
Sequential Descrambler

@author: sssan
    """
    assert isinstance(w,str)
    assert isinstance(k,tuple)
    assert(len(w) == sum(k))
    #f = open("words.txt", 'r')
    f = open(r"C:\Hari\Q5_books\143\HW4\google-10000-english-no-swears.txt",'r').read().splitlines()
    #print(f)
    dic_list=[]
    input = {}
    input ["bbeior"] =  ['robbie']
    dict1 = {}
    dict1 ["bbeior"] =  ['robbie']
    """
    for l in f:
        if len(l) in k:
            b = True
            for ll in l:
                if ll not in w:
                    b = False
                    break
            
            if(b == True):
               
                tmp = "".join(sorted(l))
                if tmp in input:
                    input[tmp].append(l)
                else:                            
                    input[tmp] = []
                    input[tmp].append(l)
    """
    
    for t in k:
     input = {}
     for l in f:
        if len(l) == t:
            b = True
            for ll in l:
                
                if ll not in w:
                    b = False
                    break
            
            if(b == True):
               
                tmp = "".join(sorted(l))
                if tmp in input:
                    input[tmp].append(l)
                else:                            
                    input[tmp] = []
                    input[tmp].append(l)    
     dic_list.append(input)
    """
    for t in k:     
        input = copy.deepcopy(dict1)
        for l in f:
            if len(l) == t:
                tmp = "".join(sorted(l))
                for d in input:
                    tmp1 = tmp + d
                    if tmp1 in input:
                        dict1[tmp1].append(l)
                    else:
                        dict1[tmp1] = []
                        dict1[tmp1].append(l)                         
     
    """
    org = w
    lis = []
    ans = ()
    #print(dic_list)
    for i,t in enumerate(dic_list):
        lis.append(range(len(dic_list[i])))
    
    lis1 = []          
    #print(lis)
    for p in product(*lis):        
        for i,itr in enumerate(p):            
            tmp = list(dic_list[i].keys())[itr]
            for dd in tmp:
                w = w.replace(dd,"",1)
        if len(w) == 0:
            #print(p)
            ans = p
                        
      
   
            for i,itr in enumerate(p):            
                tmp = list(dic_list[i].keys())[itr]
                #print(dic_list[i][tmp])
                #print(itr)
                lis1.append(range(len(dic_list[i][tmp]))) 
            break
        else:
            w = org

    #print(lis1)
    for p in product(*lis1):
        
        out_str = ""
        for j, a in enumerate(ans):
            tmp = list(dic_list[j].keys())[a]
            #print(a)
            
            #print(dic_list[j][tmp][p[j]])
            out_str = out_str + " " + dic_list[j][tmp][p[j]]
        out_str = out_str[1:]
        yield(out_str)
        
        
if __name__=='__main__':

    print(list(descrambler('choeounokeoitg',(3,5,6))))
