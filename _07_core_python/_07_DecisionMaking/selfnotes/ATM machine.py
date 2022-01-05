#ATM machine
Card = input("Please type 'card' : ")
count=0
while count<=3 :
    pin=int(input("Please enter any 3 digit PIN : "))
    if pin>99 and pin<999 :
        print("Select an option as per your wish\n\ts_no\tService\n\t1\tWithdraw\n\t2\tBalance Enquiry\n\t3\tMini Statement\n\t4\tPIN Change")
        S_no = int(input("Enter a number from the above options : "))
        if S_no==1 :
            print("\t1.Savings Account\n\t2.Current Account")
            a_c = int(input("Please select your a/c type : "))
            if a_c==1 :
                amount=int(input("Enter the amount you want : "))
                print("Please collect your amount and card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
            else :
                amount=int(input("Enter the amount you want : "))
                print("Please collect your amount and card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
                
        elif S_no==2 :
            print("Do you want to check Balance...??\nIf Yes type 'Y' other wise type 'N' ")
            ch=input("Please enter 'Y or 'N' : ")
            if ch=="Y" :
                print("Your a/c balance is xxxxxxx")
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
            else :
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
        
        elif S_no==3 :
            print("Do you want mini statement...??\nIf Yes type 'Y' other wise type 'N' ")
            ch=input('Enter "Y" or "N" : ')
            if ch=="Y" :
                print("Your transaction details are displayed")
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
            else :
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")        
                break
        elif S_no==4 :
            print("Do you want to change your PIN..???\nIf Yes type 'Y' other wise type 'N'")
            ch=input("Enter 'Y' or'N' : ")
            if ch=="Y" :
                print("Please enter your old PIN")
                print("Please enter new PIN")
                print("Your PIN has been changed")
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
            else :
                print("Please collect your card")
                print("*******THANKS FOR USING OUR ATM*******")
                break
        else :
            print("We are not providing that service right now")
            print("Please collect your card")
            print("*******THANKS FOR USING OUR ATM*******")
            break
            
    else :
        count=count+1
        print('Please enter valid password')
        if count==3:
            print("Your card has been blocked for 24Hrs")
            break

        
    
