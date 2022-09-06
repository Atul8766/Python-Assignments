def palindrome(s):
    s1 = s[::-1]  
    if(s==s1):
        print("Palindrome")
    else:
        print("Not a palindrome")

s1 = "racecar"
palindrome(s1)
