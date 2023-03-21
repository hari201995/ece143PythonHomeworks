from fractions import Fraction
import math
class Rational(object):
    def __init__(self,a,b):
        """class of rational numbers (ratio of integers) with the 
        following interfaces and behaviours
        :a: integer
        :b: integer
        """
        assert isinstance(a,int)
        assert isinstance(b,int)
        self.fraction = Fraction(a,b)
    
    def __repr__(self):
        return f'{self.fraction}'
    
    def  __eq__(self,others):
        if self.fraction==others.fraction:
            return True
        else:
            return False

    def __mul__(self,other):
        if type(other)==Rational:
            ans = self.fraction*other.fraction
        elif type(other)==int or type(other)==float:
            temp = Rational(other,1)
            ans = self.fraction* temp.fraction

        return Rational(ans.numerator,ans.denominator)
    
    def __sub__(self,other):
        ans  = self.fraction - other.fraction
        return Rational(ans.numerator,ans.denominator)
    
    
    def __neg__(self):
        temp = -1*self.fraction
        return Rational(temp.numerator,temp.denominator)
        
    def __div__(self,others):
        temp = self.fraction/others.fraction
        return Rational(temp.numerator,temp.denominator)
    
    def __rtruediv__(self,others):
        temp = others/self.fraction
        return Rational(temp.numerator,temp.denominator)
    
    def __truediv__(self,others):
        temp = self.fraction/others
        return Rational(temp.numerator,temp.denominator)

    def __add__(self,others):
        if type(others)==Rational:
            temp = self.fraction + others.fraction
        else: 
            temp = self.fraction + others
        return Rational(temp.numerator, temp.denominator)
    
    def __lt__(self,other):
        return self.fraction < other.fraction          
    

    def __int__(self):
        return int(self.fraction)
    
    def __float__(self):
        return float(self.fraction)

def square_root_rational(x,abs_tol=Rational(1,1000)):
    ''' takes an input rational number x and returns the square root
    of x to absolute precision abs_tol.
    :ob1: input object
    :abs_tol: tolerance level
    '''
    assert isinstance(x,Rational) and isinstance(x,Rational),'wrong type'

    num = x.fraction
    if x.fraction>1:
            bounds = [0,x.fraction]
            while True:
                midPoint = (bounds[0] + bounds[1])*0.5
                squareOfMidPt = midPoint * midPoint
                delta = squareOfMidPt-num
                if abs(midPoint**2-num) <= abs_tol.fraction:
                    break
                bounds[delta > 0] = midPoint
    else:
            bounds = [x.fraction,1]
            while True:
                midPoint = (bounds[0] + bounds[1])*0.5
                squareOfMidPt = midPoint * midPoint
                delta = squareOfMidPt-num
                if abs(midPoint**2-num) <= abs_tol.fraction:
                    break
                if delta > 0:
                    bounds[1] = midPoint
                else:
                    bounds[0] = midPoint
    midPoint = Fraction(midPoint)
    return Rational(midPoint.numerator,midPoint.denominator)

    
if __name__ == '__main__':
    p=square_root_rational(Rational(100,1),abs_tol=Rational(1,1000))
    print(float(p.fraction))

