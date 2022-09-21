print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divison")
num = int(input("Enter Your Choice: "))

if(num==1):
    try:
        a = int(input("Enter two numbers: "))
        b = int(input())
        print("Sum is:", a+b)
    except Exception:
        print("Please Enter numbers")
elif(num==2):
    try:
        a = int(input("Enter two numbers: "))
        b = int(input())
        print("Sum is:", a-b)
    except Exception:
        print("Please Enter numbers")
elif(num==3):
    try:
        a = int(input("Enter two numbers: "))
        b = int(input())
        print("Sum is:", a*b)
    except Exception:
        print("Please Enter numbers")
elif(num==4):
    try:
        a = int(input("Enter two numbers: "))
        b = int(input())
        print("Sum is:", a/b)
    except Exception:
        print("Please Enter numbers")