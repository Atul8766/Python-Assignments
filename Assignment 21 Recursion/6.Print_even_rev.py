def natural(num):
    if(num>0):
        print(2*num,end=" ")
        natural(num-1)
natural(10)