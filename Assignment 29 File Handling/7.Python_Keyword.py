def search(filename,list):
    try:
        f=open(filename,'r')
        count = 0
        for line in f.readlines():
            strlist=line.split(' ')
            for word in list:
                for e in strlist:
                    if(e==word):
                        count+=1
        print("There are",count,"keywords") 
    except FileNotFoundError:
        print("File not found")
        f.close()

keys=['break','continue','true','false','and','or','not','for','while','def','class','if','else','elif','import','from','except','print','return','yield','lambda','global']
search('test.py',keys)