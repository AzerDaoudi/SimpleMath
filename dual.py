#More information may be found in the Notebooks folder. Please check it

import math
import random
class Dual:
    """Class represents a simple dual number with its arithmetic rules"""
    
    def __init__(self,a = 0 , b = 0):
        if not(isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Dual does not take non-integer or float args")   
        self.re = a
        self.du = b 
        
    def __add__(self,other):

        other = self.cast(other)
        return Dual(self.re + other.re, self.du + other.du)
    
    def __sub__(self,other):
        
        other = self.cast(other)
        return Dual(self.re - other.re, self.du - other.du)
    
    def __mul__(self,other):
        other = self.cast(other)
        return Dual(self.re * other.re, self.re * other.du + self.du * other.re)
    
    def __truediv__(self,other):
        other = self.cast(other)
        if other.re != 0:
            return Dual(self.re/other.re, (self.du*other.re - self.re*other.du)/(other.re **2))
        else:
            
            if other.du != 0 and self.re == 0:
                return Dual(self.du/other.du, random.normalvariate(0,1))
            else:
                raise Exception("Division not definied")
                
    def __neg__(self):
        return Dual(-self.re, -self.du)
                    
    def __radd__(self,other):
        return self + other
    
    def __rmul__(self,other):
        return self * other
    
    def __rsub__(self,other):
        other = self.cast(other)
        return other - self
    
    
    def __rtruediv__(self,other):
        other = self.cast(other)
        return other/self
    
    
    def __abs__(self):
        return abs(self.re)
    
    def __eq__(self, other):
        return self.re == other.re and self.du == other.du
    
    def __pow__(self,x):
        return self.exp(x * self.log(self))

    
    def __repr__(self):
        if self.du >= 0:
            return f"{self.re} + {self.du}ε"
        else:
            return f"{self.re} - {abs(self.du)}ε"
        
    
    def conjugate(self):
        return Dual(self.re, -self.du)
    
    @staticmethod
    def cast(number):
        if isinstance(number, Dual):
            return number
        elif isinstance(number, (int, float)):
            return Dual(number,0)
        else:
            raise TypeError(f"can't convert {type(number)} to Dual")
            
    @staticmethod
    def exp(x):
        """Dual Method represents the dual exponential function"""
        return Dual(math.exp(x.re), math.exp(x.re) * x.du)

    @staticmethod
    def log(x):
        """Dual Method represents the dual logarithmic function"""
        return Dual(math.log(x.re),  x.du/x.re)


if __name__ == "__main__":
    #simple example of the derivative of the function f(x) = x + ln(x) at point 0.5
    x = Dual(0.5,1)
    f = lambda x: x + Dual.log(x)
    print("the derivative of f at 0.5 is : ",f(x).du) 