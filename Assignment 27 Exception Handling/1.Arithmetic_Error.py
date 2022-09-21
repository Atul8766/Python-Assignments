a = 5
b = 0
c = 0
c = a/b
print(c)
try:
    c = a/b

except ZeroDivisionError:
    print("You cannot divide by zero")


print(c)
print("Bye")