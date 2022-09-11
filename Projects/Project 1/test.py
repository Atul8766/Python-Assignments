import random
import os
def show():
    os.system('clear')
    print("\033[1;33;10m      ****************** WELCOME TO WORD PUZZLE GAME ******************\n\n\n")
def game(l1,l2):
    count = 0
    for e in random.sample(l1,5):
        print("\033[1;36;20mArrange the letters to form a valid word:")
        print(e,end='\n')
        s1=(str.upper((input())))
        for s in l2:
            if(s==s1):
                print("\033[1;32;15m\nCorrect")
                count+=1
                break
        else:
            print("\033[1;31;20m\nWrong")
            count-=1
        print("\n")
    print("\033[1;32;40mNet Score is",count)


l2 = ['FATHER','BREAK','GREEN','AEROPLANE','BOOK']
l1 = ['RENEG','RAEHTF','KABRE','OAERELANP','KOBO']
while True:
    show()
    game(l1,l2)
    print("Play again press y else n [y/n]: ")
    s = str(input())
    if (s=='y' or s=='Y'):
        pass
    else:
        break






    