#To display a grade
percentage = float(input("Enter the percentage : "))
if percentage>100 :
    print("Invalid data")
else :
    if percentage>80 :
        print("You got a grade of A+")
    elif percentage>60 :
        print("You got a grade of A")
    elif percentage>50 :
        print("You got a grade of B+")
    elif percentage>45 :
        print("You got a grade of B")
    elif percentage>25 :
        print("You got a grade of C")
    else:
        print("You got a grade of D")