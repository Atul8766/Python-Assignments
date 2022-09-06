def natural(n,num):
    if(num>0):
        natural(n,num-1)
        print(num*n,end=" ")

natural(6,5)