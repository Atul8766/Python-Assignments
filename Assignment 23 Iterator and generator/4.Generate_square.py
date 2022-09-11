def sqproducer(n):
    a=1
    while n:
        yield a*a
        a+=1
        n-=1
        
for e in sqproducer(10):
    print(e,end=' ')
    