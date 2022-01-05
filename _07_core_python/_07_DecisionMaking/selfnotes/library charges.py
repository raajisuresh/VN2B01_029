#Calculating library charges
no_of_days = int(input("How many days you want to take our service..??.."))
if no_of_days<=0 :
    print("No need to pay")
else :
    if no_of_days<=5 :
        charges = no_of_days*2
        print("You have to pay Rs 2/day\nTotal charge is Rs/-",charges)
    elif no_of_days<=10 :
        charges = no_of_days*3
        print("You have to pay Rs 3/day\nTotal charge is Rs/-",charges)
    elif no_of_days<=15 :
        charges = no_of_days*4
        print("You have to pay Rs 4/day\nTotal charge is Rs/-",charges)
    else :
        charges = no_of_days*5
        print("You have to pay Rs 5/day\nTotal charge is Rs/-",charges)