class Profile:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    def display(self):
        print("Name  : ",self.name)
        print("Age   : ",self.age)
        print("Email : ",self.email)

user1 = Profile("Atul",19,"shukla@gmail.com")
user1.display()