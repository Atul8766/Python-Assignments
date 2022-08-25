sum = 0
n = (int(input("Enter a number: ")))
while(n):
    k = n%10
    sum = sum+k
    n = int(n/10)
print("Sum is:",sum)