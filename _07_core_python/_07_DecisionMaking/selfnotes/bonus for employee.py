#To take decision on bonus amount
Service = float(input("What is the service period of an employee..??..."))
Salary = float(input("What is the salary of an employee....??.."))
if Service>10 :
    Bonus_amount = Salary*0.1
    print("Congratulations!!!!\nYou are getting bonus of Rs/-",Bonus_amount)
elif Service>=6 and Service<=10 :
    Bonus_amount = Salary*0.08
    print("Congratulations!!!!\nYou are getting bonus of Rs/-",Bonus_amount)
else :
    Bonus_amount = Salary*0.05
    print("Congratulations!!!!\nYou are getting bonus of Rs/-",Bonus_amount)


    