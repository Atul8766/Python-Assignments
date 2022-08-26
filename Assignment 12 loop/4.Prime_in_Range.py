lower = int(input("Enter lower and upper bound: "))
upper = int(input())
for i in range(lower,upper+1,1):
    for j in range(2,upper+1,1):
        if(i%j==0):
            break
    if(i==j):
       print(i,end=" ")
