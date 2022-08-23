color = str(input("Enter color: "))
match "yellow" in color:
    case 1: print("Monday")
    
match "blue" in color:
    case 1: print("Tuesday")
    
match "orange" in color:
    case 1: print("Wednesday")

match "white" in color:
    case 1: print("Thursday")
    
match "black" in color:
    case 1: print("Friday")
    
match "red" in color:
    case 1: print("Saturday")

match "" not in color:
    case 1: print("Sunday")
       
