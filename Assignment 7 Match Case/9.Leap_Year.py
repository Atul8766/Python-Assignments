year = eval(input("Enter year: "))
match year%4!=0 and year%100==0 and year%400==0:
    case 1: print("Non century leap year")
match year%4==0 and year%100==0 and year%400==0:
    case 1: print("Century leap year")
match year%4!=0 and year%100!=0 and year%400!=0:
    case 1: print("Non century non leap year")
match year%4==0 and year%100==0 and year%400!=0:
    case 1: print("Century non leap year")
    
