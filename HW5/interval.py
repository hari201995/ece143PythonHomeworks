class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b

    def __eq__(self,other):
        ''' Checks if two objects are equal
        :self Param: input object
        :other Param: input Object
        '''
        if(self._a==other._a) and (self._b==other._b):
            return True
        else:
            return False
    def __add__(self,other):
        '''main purpose of this class is to simplify overlapping continuous intervals
        :self Param: input object
        :other Param: input Object
        '''
        if(self==other):
            return self

        if (self._a<=other._a):
            if(other._a<self._b) and (other._b<=self._b):
                return self
            elif(other._a<self._b) and(other._b>self._b):
                temp=Interval(self._a,other._b)
                return temp
        elif (self._a >= other._a):
            if(self._a<other._b) and (self._b<=other._b):
                return other
            elif(self._a<other._b) and(self._b>other._b):
                temp=Interval(other._a,self._b)
                return temp
        return [self,other]


if __name__=='__main__':
    obj1 = Interval(2,3)
    obj2 = Interval(1,2)
    obj3 = Interval(5,10)
    obj4 = obj1 + obj2
    obj5 = obj2 + obj3
    print(vars(obj4))
    print(vars(obj5))