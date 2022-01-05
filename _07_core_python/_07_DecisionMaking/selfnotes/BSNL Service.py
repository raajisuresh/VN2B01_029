#BSNL Service
print("\tCATEGORY")
print("\t--------------------")
print("\t1.Commercial\n\t2.Institution\n\t3.Domestic")
print("\t--------------------")
category = int(input("Please select a category number under which you are..."))
if category==1 :
    print("You are in the category of commercial,if yes enter Y otherwise enter N")
    ch=input("Please enter 'Y' or 'N' : ")
    if ch=='Y' :
        units=int(input("Ask the customers for required no.of units : "))
        if units<=5000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Your total bill amount : 1500")
            print("------------------------------------------------")
        elif units>5000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.25)
            print("Your total bill amount : ",1500+(units-5000)*0.25)
            print("------------------------------------------------")
        elif units<=10000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.23)
            print("Your total bill amount : ",1500+(units-5000)*0.23) 
            print("------------------------------------------------")
        else :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.20)
            print("Your total bill amount : ",1500+(units-10000)*0.20)
            print("------------------------------------------------")
    else :
        print("Please select another category")
elif category==2 :
    print("You are in the category of Institutional,if yes enter Y otherwise enter N")
    ch=input("Please enter 'Y' or 'N' : ")
    if ch=='Y' :
        units=int(input("Ask the customers for required no.of units : "))
        if units<=5000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Your total bill amount : 1800")
            print("------------------------------------------------")
        elif units>5000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.30)
            print("Your total bill amount : ",1800+(units-5000)*0.30)
            print("------------------------------------------------")
        elif units<=10000 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.28)
            print("Your total bill amount : ",1800+(units_5000)*0.28)
            print("------------------------------------------------")
        else :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",0.25)
            print("Your total bill amount : ",1800(units-10000)*0.25)
            print("------------------------------------------------")
    else :
        print("Please select another category")
elif category==3 :
    print("You are in the category of Domestic,if yes enter Y otherwise enter N")
    ch=input("Please enter 'Y' or 'N' : ")
    if ch=='Y' :
        units=int(input("Ask the customers for required no.of units : "))
        if units<=100 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Your total bill amount : 75") 
            print("------------------------------------------------")
        elif units>100 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",1.25)
            print("Your total bill amount : ",75+(units-100)*1.25)
            print("------------------------------------------------")
        elif units<=200 :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",2.00)
            print("Your total bill amount : ",75+(units-100)*2.00)
            print("------------------------------------------------")
        else :
            print("------------------------------------------------")
            print("Total no.of units you have consumed : ",units)
            print("Service charge per unit : ",2.50)
            print("Your total bill amount : ",75+(units-200)*2.50)
            print("------------------------------------------------")
    else :
        print("Please select another category")
else :
    print("We are not giving service to your category")