class Employee:
    __companyname = "Shukla Bros"

    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def display(self):
        print("Company       :  ",Employee.__companyname,end="\n")
        print("Employee id   :  ",self.empid)
        print("Employee Name :  ",self.name)
        print("Emplyee Salary:  ",self.salary)

emp1 = Employee(125,"Subhash",15000)
emp2 = Employee(128,"Kamal",18000)

emp1.display()
emp2.display()