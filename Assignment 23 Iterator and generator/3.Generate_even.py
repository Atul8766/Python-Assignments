def evenproducer(n):
    a = 2
    while n:
        yield a
        a+=2
        n-=1

for e in evenproducer(10):
    print(e,end=" ")
    