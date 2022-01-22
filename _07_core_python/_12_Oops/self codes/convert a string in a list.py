#convert a string in a list
#By using class and object approach
print("By using class and object")
class String_to_list:
    def __init__(self):
        pass
    def str_lst(self):
        self.str3=input("Enter a line of text : ")
        self.list=[]
        for i in self.str3:
            self.list.append(i)
        print(self.list)

str_list=String_to_list()
str_list.str_lst()
print('='*50)