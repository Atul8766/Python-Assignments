class User:
    def __init__(self,name,age,email):
        self.n = name
        self.a = age
        self.e = email 

def youngest(user1,user2,user3):
    if(user1.a<user2.a):
        if(user1.a<user3.a):
            print(user1.n,"is Youngest of all")
    elif(user2.a<user3.a):
        print(user2.n,"is Youngest of all")
    else:
        print(user3.n,"is Youngest of all")

user1 = User("Atul",15,'shukla@gmail.com')
user2 = User("Navin",10,'reddy@ineuron.ai')
user3 = User("Kuch Bhi",5,"kuchto@gmail.com")
youngest(user1,user2,user3)
