#Retriving image from a location
file=open('C:/Users/LENOVO/Desktop/IMG-20181231-WA0003.jpg','rb')
file1=open('life.jpg','wb')
for bytes in file:
    file1.write(bytes)