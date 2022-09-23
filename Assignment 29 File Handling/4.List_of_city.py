def writing(filename,text):
    with open(filename,'w') as f:
        for word in text:
            f.write("%s\n"%word)
city = ['Indore','Bhopal','Dewas','Rewari','Chandigarh']
writing('cities.txt',city)