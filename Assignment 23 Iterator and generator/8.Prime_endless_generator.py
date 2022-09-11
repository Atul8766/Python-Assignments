import sys
def prime():
    for e in range(2,sys.maxsize**10):
        for a in range(2,sys.maxsize**10):
            if(e%a==0):
                break
        if(e==a):
            yield a

it = prime()
l1 = []
while True:
    ans  = input("Enter y to  generate element n to stop: ")
    if(ans=='y'):
        x = next(it)
        print(x)
        l1.append(x)
    else:
        print(l1)
        break