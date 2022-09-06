def count(s):
    lowercase = 0
    uppercase = 0
    for e in s:
        if(e>='A' and e<='Z'):
            uppercase+=1
        elif(e>='a' and e<='z'):
            lowercase+=1
    print("There are",uppercase,"uppercase","and",lowercase,"lowercase")

s1 = "Atul Shukla"
count(s1)
