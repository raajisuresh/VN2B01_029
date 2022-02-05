#Count characters in string
#By using class and method approach
class Count:
    def string(self):
        self.string=input('Enter a text : ')
    def count(self):
        character1=input("Enter a character from above count to count its occurences in text : ")
        self.count1=0
        for element in self.string:
            if element==character1:
                self.count1+=1
            else:
                pass
        print("Count of a given character is {}.".format(self.count1))
        #return self.count1

count=Count()
count.string()
count.count()