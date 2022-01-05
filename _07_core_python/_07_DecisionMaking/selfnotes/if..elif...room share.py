#PG room sharing Name = input('Enter your name : ')
contact_no = int(input('Enter your phone number : '))
print('=======================================================')
print('=======================================================')
print("***** YOU ARE SUCCESSFULLY REGISTERED*****")
print("ENTER AMOUNT FOR ROOM SHARING IN BETWEEN 6K TO 12K")
print('=======================================================')
print('=======================================================')
rent_amount = int(input("Amount : "))
if rent_amount==6000 :
    print("You will get a 'THREE sharing' room")
elif rent_amount==7000 :
    print("You will get a 'TWO sharing' room")
elif rent_amount==10000 :
    print("You will get 'SEPERATE' room for you 'ONLY' ")
elif rent_amount>10000 and rent_amount<=12000 :
    print("You will get 'EXTRA FACILITIES' with a 'SEPERATE' room")
else :
    print('=======================================================')
    print("ThanQ for your intrest")
    print("Right now we are unable to give service in this amount")
print('=======================================================')
