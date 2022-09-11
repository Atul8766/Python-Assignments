def oddproducer(n):
    a = 1
    while n:
        yield a
        a+=2
        n-=1

for e in oddproducer(10):
    print(e,end=" ")
    