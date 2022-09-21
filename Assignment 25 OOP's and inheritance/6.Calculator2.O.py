class Calculator:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        x = self.x+other.x
        return x
    def __sub__(self,other):
        x = self.x-other.x
        return x
class Calculator2_O(Calculator):
    def __init__(self,x):
        self.x = x
    def __mul__(self,other):
        x = self.x*other.x
        return x
    def __div__(self,other):
        x = self.x/other.x
        return x

num1 = Calculator2_O(5)
num2 = Calculator2_O(5)

num3 = num1*num1
num4 = num1/num2
print(num4)