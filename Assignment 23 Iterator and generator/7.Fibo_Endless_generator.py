def fiboproducer():
    a,b=0,1
    while True:
        yield a
        a,b=a+b,a

it = fiboproducer()
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