num1=int(input("Enter a number : "))
while True:
    op=input("Select +,-,*,/,= any one : ")
    if op=='=':
        print(num1)
        break
    elif op=='+':
        num2=int(input("Enter a number : "))
        sum=num1+num2
        num1=sum
    elif op=='-':
        num2=int(input("Enter a number : "))
        diff=num1-num2
        num1=diff
    elif op=='*':
        num2=int(input("Enter a number : "))
        product=num1*num2
        num1=product
    elif op=='/' :
        num1=int(input("Enter a number : "))
        div=num1/num2
        num1=div
    else :
        print('select valid operator')
