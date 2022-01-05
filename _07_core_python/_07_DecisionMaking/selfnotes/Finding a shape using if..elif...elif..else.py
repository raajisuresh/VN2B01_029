#Finding a shape
no_sides=int(input("Enter no.of sides : "))
if no_sides<0 or no_sides==1 or no_sides==2 :
    print("Try again for another shape")
elif no_sides==0 :
    print("Its a circle")
elif no_sides==3 :
    print("Its a triangle")
elif no_sides==4 :
    print("Its a square or rectangle")
elif no_sides==5 :
    print("Its a pentagon")
elif no_sides==6 :
    print("Its  a heptagon")
elif no_sides==7 :
    print("Its a heptagon")
elif no_sides==8 :
    print("Its an octagon")
elif no_sides==9 :
    print('Its anonagon')
elif no_sides==10 :
    print('Its a decagon')
else :
    print("your are asking for more number of sides")