def prime(num):
    for x in range(2,num,1):
       if(num%(x+1)==0):
           break
    if(num==(x+1)):
        print("Prime")
    else:
        print("Not Prime")

prime(10)