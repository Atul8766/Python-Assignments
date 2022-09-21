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
class Phone:
    def call(self):
        print("calling.....")
    def sms(self):
        print("sms.....")

class SmartPhone(Phone,Calculator2_O):
    def videocall(self):
        print("Video Call.....")


phone1 = SmartPhone()
# phone1.__add__(2,4)