#finding a number prime or not
num = int(input("Enter a number : "))
if num%2==0 or num%3==0  or num%5==0 or num%7==0 :
    if num%2==0 and num%3==0 :
        print("It is a prime number")
    elif num%5==0 and num%7==0 :
        print("It is a prime number")
    else :
        print("It is a prime number")
else :
    print("It is a prime number")