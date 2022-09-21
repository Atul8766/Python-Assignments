
class School:
    __name = "Education System Public School"
    def __init__(self,student_name,student_rollno,student_class):
        self.student_name = student_name
        self.student_rollno = student_rollno
        self.student_class = student_class
    def show(self):
        print("School Name : ",School.__name)
        print("Student Name : ",self.student_name)
        print("Student Roll No : ",self.student_rollno)
        print("Student Class : ",self.student_class,"th",sep="")

s1 = School("Atul Shukla",24,4)
s1.show()