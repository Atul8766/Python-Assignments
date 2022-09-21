a = 5
c = 0

try:
    b = int(input("Enter a number: "))
    c = a/b
except ValueError:
    print("Please give correct input")
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception:
    print("Please Try Again....")
print(c)
print("Thanks")
