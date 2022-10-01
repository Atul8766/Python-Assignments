def pangram(s):
    pangram = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    value = 0
    for e in pangram:
        for x in s:
            if(e==x):
                count+=1
                value = value+count
            if(count==1):
                break
        count = 0
    if(value == 26):
        print("PANGRAM")
    else:
        print("Not a pangram")



s1 = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
s2 = "The quick brown fox jumps over the lazy dog"
pangram(s2)