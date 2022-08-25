fact = 1
for x in range(int(input("Enter a number: ")),1,-1):
        fact = fact*((x+1)-1)
print("Factorial is:",fact)