lower = int(input("Enter a number: "))
for i in range(lower,lower+lower,1):
    for j in range(2,lower+lower,1):
        if(i%j==0):
            break
    if(i==j):
       print("Next Prime no is:",i,end="\n")
       break
