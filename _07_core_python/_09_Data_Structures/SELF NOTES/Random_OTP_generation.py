#Random OTP generation
set={'a',8,'b','A','c','D','F','V',7,'d','K','x',6,'z','e','q',9,'y','i','g'}
OTP=str()
n=int(input("Enter the length of otp : "))
for i in range(0,n):
    otp=set.pop()
    OTP=OTP+str(otp)
print("\t","_"*50)
print('\t  Generated OTP : ',OTP)
print("\t","_"*50)

