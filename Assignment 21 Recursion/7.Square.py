def natural(num):
    if(num>0):
        natural(num-1)
        print(num**2,end=" ")

natural(10)