#fibanocci series
first_number=int(input("enter first number : "))
second_number=int(input("enter second number : "))
count=2
n=int(input("Enter length of series : "))
print("Fibanocci series-----------")
print(first_number)
print(second_number)
while count<=n :
    third_number=first_number+second_number
    print(third_number)
    first_number=second_number
    second_number=third_number
    count+=1







#0,1,1,2,3,5,8

