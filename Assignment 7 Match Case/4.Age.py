age = eval(input("Enter Age: "))
match age>0 and age<10:
    case 1: print("Kid")
match age>=10 and age<20:
    case 1: print("Teen")
match age>=20 and age<40:
    case 1: print("Young")
match age>=40 and age<60:
    case 1: print("Experienced")
match age>=60:
    case 1: print("Senior Citizen")    

    
