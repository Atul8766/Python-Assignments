
import pickle


f = open('bookdata','rb')
s = pickle.load(f)
for key in s:
    print(key," ",s[key])
f.close()