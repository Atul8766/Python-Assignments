n = int(input("Enter a number: "))
for x in range(1,n,1):
    if(n%(x+1)==0):
        break
if(n==(x+1)):
    print("Prime")
else:
    print("Not Prime")