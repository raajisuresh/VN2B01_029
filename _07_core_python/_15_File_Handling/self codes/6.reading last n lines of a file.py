#reading n lines of a file
class FileReading:
    def no_lines(self):
        self.file=open('C:/Users/LENOVO/Desktop/oops.txt','r')
        self.count=0
        for i in self.file:
            self.count+=1
        return self.count
    def first_n_lines(self):
        self.file=open('C:/Users/LENOVO/Desktop/oops.txt','r')
        self.n=int(input("Enter how many lines u want from starting : "))
        count=0
        for i in self.file:
            if count<self.n:
                print(i)
            count+=1
    def last_n_lines(self):
        self.file=open('C:/Users/LENOVO/Desktop/oops.txt','r')
        self.m=int(input("Enter how many lines u want at last : "))
        count_=0
        for i in self.file:
            count_+=1
            if count_>self.count-self.m:
                print(i)
    def required_lines(self):
        self.file=open('C:/Users/LENOVO/Desktop/oops.txt','r')
        self.m=int(input("Enter staring line : "))
        self.n=int(input("Enter ending line : "))
        count=0
        for i in self.file:
            if self.m<count<self.n :
                print(i)
            count+=1
try:
    data=FileReading()
    print("No.of lines in given file are ",data.no_lines())
    print("_"*70)
    data.first_n_lines()
    print("_"*70)
    data.last_n_lines()
    print("_"*70)
    data.required_lines()
    print("_"*70)
except FileNotFoundError:
    print("Your file is not found")