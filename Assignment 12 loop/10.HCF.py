a = int(input("Enter pair of numbers: "))
b = int(input())
ans = 0
for i in range (1,1000,1):
    if(a%i==0 and b%i==0):
        ans = i

print("HCF is",ans,"\n")