def min(a,b,c):
    if(a<b):
        if(a<c):
            print(a)
        else:
            print(c)
    elif(b<c):
        print(b)
    else: 
        print(c)


min(1,0,-1)