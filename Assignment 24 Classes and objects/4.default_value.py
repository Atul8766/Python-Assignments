class User:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)        

user1 = User(1,2)
user1.show()

