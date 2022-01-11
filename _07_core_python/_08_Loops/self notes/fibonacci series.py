#fibanocci series
first_number=int(input("enter first number : "))
second_number=int(input("enter second number : "))
count=0
n=int(input("Enter length of series : "))
print("Fibanocci series-----------")
while count<n :
    print(first_number)
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number
    count+=1








