a = int(input("Enter pair of numbers: "))
b = int(input())
ans = 0
for i in range (1,1000,1):
    if(i%a==0 and i%b==0):
        ans = i

print("LCM is",ans,"\n")