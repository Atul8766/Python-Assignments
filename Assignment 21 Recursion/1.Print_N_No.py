def natural(num):
    if(num>0):
        natural(num-1)
        print(num,end=" ")

natural(10)
