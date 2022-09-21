a = 5
c = 0

try:
    b = int(input("Enter a number: "))
    c = a/b

except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Please Enter Only Numbers")

print(c)
print("Bye")