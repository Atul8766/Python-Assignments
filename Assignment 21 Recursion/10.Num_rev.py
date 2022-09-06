def natural(num):
    if(num==0):
        return 0
    print(num%10,end="")
    natural(int(num/10))

natural(5684)
print()