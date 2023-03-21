import copy

class Polynomial(object):
    ''' class that can implement a univariate polynomial (Polynomial)
    over the field of integers (only!)
    '''

    def __init__(self,coeff):
        '''class of rational numbers (ratio of integers) with the 
        following interfaces and behaviours
        '''
        assert isinstance(coeff,dict),'Wrong input'
        for key,value in coeff.items():
            if isinstance(key,int):
                if key<0:
                    assert 0,'Wrong input'
            else:
                assert 0,'wrong input'
            if isinstance(value,int):
                pass
            else:
                assert 0,'wrong input'
        self._pOfX = coeff
    

    def __repr__(self):
        out =[]
        pofX = dict(sorted(self._pOfX.items()))
        finalStr= ''
        for key,values in pofX.items():
            temp = []
            if key==0:
                if values!=0:
                    temp = str(abs(values))
            elif key==1:
                if values !=1:
                    if values !=0:
                        temp = str(abs(values)) + ' ' + 'x'
                if values ==1:
                    temp = 'x'
            else:
                if values !=0:
                    if values !=1:
                        temp = str(abs(values)) + ' ' + 'x' + '^'+ '(' + f'{key}' + ')'
                    else:
                        temp = 'x' + '^'+ '(' + f'{key}' + ')'
            if values >0:
                finalStr = finalStr + '+' + ' ' + temp + ' '
            if values <0:
                finalStr = finalStr + '-' + ' ' +  temp + ' '
        if finalStr=='':
            finalStr = str(0)
            return finalStr
        else:
            if finalStr[0]=='+' or finalStr[1]=='-':
                finalStr = list(finalStr)[2:-1]
                finalStr = ''.join(finalStr)
            return finalStr
                        
    

    def __eq__(self,other):
        if isinstance(other,int):
            flag= True
            for key,value in self._pOfX.items():
               if key!=0:
                   if value==0:
                       flag=True
                   else:
                       return False
               else:
                   pass
            if flag==True and 0 in self._pOfX.keys() and self._pOfX[0]==other:
                return True
            elif flag==True and 0 not in self._pOfX.keys() and other==0:
                return True
            else:
                return False
        elif isinstance(other,Polynomial):
            keyLim1 = max(self._pOfX.keys())
            keyLim2 = max(other._pOfX.keys())
            maxKeyLim = max(keyLim1,keyLim2)
            objSelf = copy.deepcopy(self)
            objOther = copy.deepcopy(other)
            for i in range(maxKeyLim+1):
                if i not in objSelf._pOfX.keys():
                    objSelf._pOfX[i]=0
                if i not in objOther._pOfX.keys():
                    objOther._pOfX[i]=0
            if objSelf._pOfX == objOther._pOfX:
                return True
            else:
                return False


            
    def __add__(self,other):
        result = {}
        if isinstance(other,Polynomial):
            commonPowers = list(set(self._pOfX.keys()) & set(other._pOfX.keys()))
            noncommonPowers = list(set(self._pOfX.keys()) ^ set(other._pOfX.keys()))
            for elm in commonPowers:
                result[elm] = self._pOfX[elm] + other._pOfX[elm]
            for elm in noncommonPowers:
                if elm in self._pOfX.keys():
                    result[elm] = self._pOfX[elm]
                elif elm in other._pOfX.keys():
                    result[elm] = other._pOfX[elm]
            sumPOfX = Polynomial(result)
            return sumPOfX
        elif (isinstance(other,int)):
            result = self._pOfX.copy()
            if 0 in self._pOfX.keys():
                result[0] = self._pOfX[0] + other
                sumPOfX = Polynomial(result)
            else:
                result[0] = other
                sumPOfX = Polynomial(result)
            return sumPOfX
        else:
            raise NotImplementedError
    
    def __radd__(self,c):
        if isinstance(c,int):
            pOfXCopy=copy.deepcopy(self)
            result = pOfXCopy._pOfX
            if 0 in result.keys():
                result[0] = result[0] + c
            else:
                result[0]=c
            return Polynomial(result)
        else:
            raise NotImplementedError 

    def __sub__(self,other):

        result = {}
        if isinstance(other,Polynomial):
            placeHolder = copy.deepcopy(other)
            for K,V in placeHolder._pOfX.items():
                placeHolder._pOfX[K]=-1*V

            commonPowers = list(set(self._pOfX.keys()) & set(placeHolder._pOfX.keys()))
            noncommonPowers = list(set(self._pOfX.keys()) ^ set(placeHolder._pOfX.keys()))
            for elm in commonPowers:
                result[elm] = self._pOfX[elm] + placeHolder._pOfX[elm]
            for elm in noncommonPowers:
                if elm in self._pOfX.keys():
                    result[elm] = self._pOfX[elm]
                elif elm in other._pOfX.keys():
                    result[elm] = placeHolder._pOfX[elm]
            sumPOfX = Polynomial(result)
            return sumPOfX
        elif (isinstance(other,int)):
            result = self._pOfX.copy()
            if 0 in self._pOfX.keys():
                result[0] = self._pOfX[0] - other
                sumPOfX = Polynomial(result)
            else:
                result[0] = -1*other
                sumPOfX = Polynomial(result)
            return sumPOfX
        else:
            raise NotImplementedError


    def __rsub__(self,c):
        if(isinstance(c,int)):
            result = self._pOfX.copy()
            for K,V in result.items():
                result[K]=-1*V
            if 0 in self._pOfX.keys():
                result[0] = c - self._pOfX[0]
                sumPOfX = Polynomial(result)
            else:
                result[0] = 1*c
                sumPOfX = Polynomial(result)
            return sumPOfX
        else: 
            raise NotImplementedError
    

    def  __mul__(self,other):
        result = {}
        if isinstance(other,Polynomial):
            maxPower = max(self._pOfX.keys()) + max(other._pOfX.keys())
            secondPxValues = list(other._pOfX.values())
            secondPxKeys= other._pOfX.keys()
            for i in range(maxPower+1):
                result[i]=[]
            for N,V in self._pOfX.items():
                resultCoeff = [V*val for val in secondPxValues]
                newPowers = [N+ k for k in secondPxKeys]
                for i in range(len(newPowers)):
                    result[newPowers[i]].append(resultCoeff[i])
            temp = {key : sum(result[key]) for key in result.keys()}
            output = {key : value for key,value in temp.items() if value>0}
            if 0 not in output.keys():
                output[0]=0
            return Polynomial(output)
        if isinstance(other,int):
            result = self._pOfX.copy()
            for key,value in self._pOfX.items():
                result[key] = value*other
            return Polynomial(result)
        else:
            raise NotImplementedError


    def __rmul__(self,c):
        if isinstance(c,int):
            result=self._pOfX.copy()
            for key,value in self._pOfX.items():
                result[key] = value*c
            return Polynomial(result)
        else:
            raise NotImplementedError


    def subs(self,value):
        assert isinstance(value,int),'wrong input'
        result = 0
        for key,coeff in self._pOfX.items():
            result = result + (value**key)*coeff
        return result


    def __truediv__(self,other):
        if isinstance(other,int):
            result={}
            for key,value in self._pOfX.items():
                if ((value/other) % 1) ==0:
                    result[key]=int(value/other)
                else:
                    raise NotImplementedError
            return Polynomial(result)
        if isinstance(other,Polynomial):
            Pcopy = copy.deepcopy(self)
            Qcopy = copy.deepcopy(other)

            P = {}
            sortedKey = sorted(list(Pcopy._pOfX.keys()),reverse=True)
            for elm in sortedKey:
                P[elm] = Pcopy._pOfX[elm]

            Q = {}
            sortedKey = sorted(list(Qcopy._pOfX.keys()),reverse=True)
            for elm in sortedKey:
                Q[elm] = Qcopy._pOfX[elm]
            result ={}
            
            while True:
                powerOfP = list(P.keys())
                powerOfQ = list(Q.keys())
                coeffOfP = list(P.values())
                coeffOfQ = list(Q.values())
                if len(powerOfP) !=0:
                    if max(list(P.keys())) < max(list(Q.keys())):
                        if stage !=0:
                            raise NotImplementedError
                        else:
                            break
                else:
                        if stage !=0:
                            raise NotImplementedError
                        else:
                            break                   

                delRef = powerOfP[0]
                quoPower = powerOfP[0] - powerOfQ[0]
                quoCoeff = int(coeffOfP[0]) / int(coeffOfQ[0])
                if quoCoeff % 1 !=0:
                    raise NotImplementedError
                else:
                    quoCoeff = int(quoCoeff)
                result[quoPower] = quoCoeff
                tempQx = { powerOfQ[k]+ int(quoPower) : quoCoeff* coeffOfQ[k] for k in range(0,len(powerOfQ),1)}
                tempP = Polynomial(P)
                tempQ = Polynomial(tempQx)
                stage = tempP - tempQ
                P = stage._pOfX
                P= dict(sorted(P.items(), key=lambda x: -x[0]))
                del P[delRef]
            result = dict(sorted(result.items(), key=lambda x: x[0]))
            return Polynomial(result)
        
if __name__=='__main__':
   '''
   p = Polynomial({0:8,1:2,3:4})
   q = Polynomial({0:8, 1:2, 2:8, 4:4})
   print(repr(p))
   p = Polynomial({2:3,1:1})
   q = Polynomial({2:3})
   print(p-q==Polynomial({1:1}))
   print(p*3)
   print(3*p)
   print(p+q)
   print(p*4+5-3*p-1)
   print(type(p-p))
   print(p*q)
   print(p.subs(10))
   print((p-p)==0)
   print(p==q)
   p = Polynomial({0:8,1:0,3:4})
   print(repr(p))
   p=Polynomial({2:1,0:-1})
   q =Polynomial({1:1,0:-1})
   print(p/q)
   d = Polynomial({1:1})
   print(d)
   print(Polynomial({3:4,1:2})*Polynomial({1:1}))
   print((Polynomial({3:4,1:2})/Polynomial({0:1}))==Polynomial({3:4,1:2}))
   print(p/Polynomial({1:1,0:-3}))'''
   p=Polynomial({2:2,1:-2})
   d = Polynomial({1:1})
   print(p)
   print(p/d)
    
