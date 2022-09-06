def natural(num):
    if(num>0):
        natural(num-1)
        print(num**3,end=" ")

natural(10)