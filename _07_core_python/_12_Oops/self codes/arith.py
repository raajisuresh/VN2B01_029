class Operations:
    def __init__(arg,operand):
        operand=int(input("Enter a number : "))
        arg.operand=operand
    def arth(arg):
        operand2=int(input("Enter another number : "))
        operator=input("Enter an operator +,-,*,/ : ")
        if operator=='+':
            sum=arg.operand+operand2
            print(sum)
        elif operator=='-':
            diff=arg.operand-operand2
            print(diff)
        elif operator=='*':
            product=arg.operand*operand2
            print(product)
        elif operator=="/":
            div=arg.operand/operand2
            print(div)
        else:
            print("Invalid operator")
    def exponentiation(arg):
        exp=arg.operand*arg.operand
        print(exp)


operand=Operations(1)
operand.arth()


        