class Profile:
    paltform = "iNeuron"
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    def display(self):
        print("Name  : ",self.name)
        print("Age   : ",self.age)
        print("Email : ",self.email)
    @classmethod
    def static(self):
        print(Profile.paltform)

