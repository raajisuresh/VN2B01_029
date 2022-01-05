#Electricity bill calculation
units= int(input("Enter no_of units consumed : "))
if units<=100 :
    print("No service charge")
elif units>100 and units<=200:
    charge=(units-100)*5
    print("Your service charge is : ",charge)
else :
    charge=(500)+(units-200)*10
    print("Your charge is : ",charge)