import sys
def prime(n):
    count = 0
    for e in range(2,sys.maxsize**10):
        for a in range(2,sys.maxsize**10):
            if(e%a==0):
                break
        if(e==a):
            yield a
            count+=1
            if(count==n):
                break
            
for e in prime(10):
    print(e,end=' ')