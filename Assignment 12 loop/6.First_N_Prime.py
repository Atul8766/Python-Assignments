count = 0
upper = int(input("Enter a number: "))
for i in range(2,True,1):
    for j in range(2,True,1):
        if(i%j==0):
            break
    if(i==j):
       print(i,end=",")
       count+=1
       if(count==upper):
        break

print()