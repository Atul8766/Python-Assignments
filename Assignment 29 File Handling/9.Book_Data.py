import pickle

data = {'C':456,'C++':800,'Java':850}
f = open('bookdata','ab')
pickle.dump(data,f)
f.close()