def sum(n):
    if(n==0):
        return 0
    return 2*n+sum(n-1)

a =sum(5)
print(a)