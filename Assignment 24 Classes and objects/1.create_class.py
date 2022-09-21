class User:
    def __init__(self,name,age,email):
        self.n = name
        self.a = age
        self.e = email
    def show(self):
        print(self.n,self.a,self.e) 


user1 = User("Atul",15,'shukla@gmail.com')
user1.show()