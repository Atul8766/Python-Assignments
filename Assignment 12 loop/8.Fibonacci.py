n = int(input("Enter a number: "))
i=0
a,b = 0,1
print(a,b,end=" ")
while i<n-2:
    c = a+b
    print(c,end=" ")
    a = b
    b = c
    i+=1