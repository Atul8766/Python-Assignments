def bin(num):
    if(num==0):
        return 0
    bin(int(num/2))
    print(num%2,end="")

bin(18)