def oct(num):
    if(num==0):
        return 0
    oct(int(num/8))
    print(num%8,end="")

oct(18)