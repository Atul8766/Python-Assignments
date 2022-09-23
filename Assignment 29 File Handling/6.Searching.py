def search(filename,word):
    try:
        f=open(filename,'r')
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist=line.split('\n')
            word_count=0
            for w in strlist:
                word_count+=1
                if word==w:
                    return(line_count,word_count)
        else:
            return None
        f.close()
    except FileNotFoundError:
        print("File not found")

print(search('cities.txt','Dewas'))