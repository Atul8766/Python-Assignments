n = (int(input("Enter a number: ")))
print("Binary is: ",end="")
while(n):
    k = n%2
    print(k,end="")
    n = int(n/2)
print(0,end="")
   