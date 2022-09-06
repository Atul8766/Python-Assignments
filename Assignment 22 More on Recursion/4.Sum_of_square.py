def sum(n):
    if(n==1):
        return 1
    return n**2+sum(n-1)

a = sum(5)
print(a)