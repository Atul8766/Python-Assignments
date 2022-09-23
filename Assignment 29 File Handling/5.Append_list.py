def writing(filename,text):
    with open(filename,'a') as f:
        for word in text:
            f.write("%s\n"%word)
city = ['Rajsthan','Jaipur','Delhi','Gurugram','Banglore','Kolkata','Noida']
writing('cities.txt',city)