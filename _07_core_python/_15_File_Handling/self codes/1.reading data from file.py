#Reading data from file
file=open('mydata.txt','r')
n=int(input("Enter how many lines u want to read from starting : "))
read_count=0
while True:
    print(file.readlines(read_count+1))
    read_count+=1
    if read_count==n:
        break