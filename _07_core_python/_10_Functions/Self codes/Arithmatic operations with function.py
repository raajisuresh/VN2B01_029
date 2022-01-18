#Arithmatic operations with function

#function defination
def sum(a,b):
    sum=a+b
    return sum
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul
def div(a,b):
    div=a/b
    return div

#function calling
a=float(input("Enter a number : "))
b=float(input("Enter a number : "))
print("\tSelect an option from below : \n\t1.Addition\n\t2.Subtraction\n\t3.Mutiplication\n\t4.Division")
option=int(input("Please select any one from above : "))
if option==1:
    print("Addition = ",sum(a,b))
elif option==2:
    print("Difference = ",sub(a,b))
elif option==3:
    print("Product = ",mul(a,b))
elif option==4:
    if b==0:
        print("Please Enter valid number")
    else:
        print("Division = ",div(a,b))
else :
    print("Invalid option")
    
