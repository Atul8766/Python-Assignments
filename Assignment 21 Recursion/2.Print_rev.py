def natural(num):
    if(num>0):
        print(num,end=" ")
        natural(num-1)
        
natural(10)