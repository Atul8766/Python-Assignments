def natural(num):
    if(num>0):
        natural(num-1)
        print(2*num-1,end=" ")

natural(10)