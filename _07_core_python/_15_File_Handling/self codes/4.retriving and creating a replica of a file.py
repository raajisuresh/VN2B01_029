#retriving and creating replica of original file
file=open('C:/Users/LENOVO/Desktop/oops.txt','r')
file1=open('C:/Users/LENOVO/Desktop/oops_concepts.txt','w')
for bytes in file:
    file1.write(bytes)