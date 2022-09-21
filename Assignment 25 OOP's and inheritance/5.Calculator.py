class Calculator:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        x = self.x+other.x
        return x
    def __sub__(self,other):
        x = self.x-other.x
        return x


c1 = Calculator(2)
c2 = Calculator(4)

c3 = c1-c2
print(c3)
