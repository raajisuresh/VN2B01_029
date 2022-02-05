#appending data
file=open('mydata.txt','a')
n=int(input('Enter how many lines u want to append : '))
append_lines=0
while True:
    data=input("Enter info : ")
    file.writelines((data,'\n'))
    append_lines+=1
    if append_lines==n:
        break