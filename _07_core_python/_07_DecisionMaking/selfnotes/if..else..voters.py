#CHECKING ELIGIBILITY FOR VOTING IN GENERAL ELECTIONS
print("CHECKING ELIGIBILITY FOR VOTING IN GENERAL ELECTIONS")
print('=========================================================')
country=input('Enter your country name : ')
if country=='INDIA' or country=='india' :
    AGE=int(input('Enter age of an voter : '))
    if AGE<18 or AGE >100  :
        print("You are not eligible for voting")
    else :
        print("You are eligible and apply for voter-id")
else :
     print("You are not a citizen of our country")