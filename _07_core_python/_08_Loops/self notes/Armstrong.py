#armstrong number 
'''number=input("Enter a number : ")
sum=0
for i in number :
    i=int(i)
    sum=sum+i**3
print("Number is ",number)
print("sum is ",sum)
if int(number)==sum :
    print("armstrong")
else:
    print("Not an armstrong")'''


#Armstrong numbers with in a range
number=input("Enter first number : ")
num=input("Enter second number : ")
sum=0
for Number in range(int(number),int(num)):
    for i in str(Number) :
        i=int(i)
        sum=sum+i**3
    print("Number is ",Number)
    print("sum is ",sum)
    if int(i)==sum :
        print("armstrong")
        print("_"*50)
    else:
        print("Not an armstrong")
        print("_"*50)
    
