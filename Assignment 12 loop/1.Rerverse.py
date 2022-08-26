n = int(input("Enter a number: "))
print("Reverse is: ",end="")
while(n):
    k = n%10
    print(k,end="")
    n = int(n/10)
print()