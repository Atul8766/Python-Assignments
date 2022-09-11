def fiboproducer(n):
    a,b=0,1
    while n:
        yield a
        a,b=a+b,a
        n-=1
        
for e in fiboproducer(10):
    print(e,end=' ')
    