#writting from the user input into a text file
file=open('mydata.txt','w+')
n=int(input("Enter no.of lines u want to write : "))
line_count=0
while True:
    data=input("Enter the text : ")
    file.writelines((data,'\n'))
    line_count+=1
    if line_count==n:
        break
