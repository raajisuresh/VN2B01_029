avg=0
sum=0
count=0
while count<=sum:
    number=int(input("Enter a number : "))
    if number>0 :
        count=count+1
        sum=sum+number
        avg=sum/count
    else :
        break
print(sum,avg)
