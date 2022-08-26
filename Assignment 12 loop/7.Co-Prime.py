a = int(input("Enter pair of numbers: "))
b = int(input())
ans = 0
for i in range (1,a+b,1):
    if(a%i==0 and b%i==0):
        ans = i
if ans==1:
    print("Given Numbers are Co-prime\n")
else:
    print("They are not Co-prime\n")