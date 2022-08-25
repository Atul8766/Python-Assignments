n = (int(input("Enter a number: ")))
print("Octal is: ",end="")
while(n):
    k = n%8
    print(k,end="")
    n = int(n/8)
print()