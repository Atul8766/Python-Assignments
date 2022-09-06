def natural(num):
    if(num>0):
        print(2*num-1,end=" ")
        natural(num-1)
natural(10)