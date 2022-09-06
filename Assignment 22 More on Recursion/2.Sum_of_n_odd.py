def sum(n):
    if(n==0):
        return 0
    return (2*n-1)+sum(n-1)

a =sum(10)
print(a)