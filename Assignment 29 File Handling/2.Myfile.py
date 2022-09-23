def writing(filename,text):
    with open(filename,'w') as f:
        f.write(text)

writing('myfile.txt',"Hello everyone this is my new file which is made by python")