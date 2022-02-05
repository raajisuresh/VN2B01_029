import random
class _Person_details:
    def __init__(self):
        pass
    def details(self,name,mobile_num,address):
        self.name=name
        self.name=input("Enter your name : ")
        self.mobile_num=mobile_num
        self.mobile_num=int(input("Enter mobile number : "))
        self.address=address
        self.address=input("Enter address : ")
        print("Name : ",self.name,"\nMobile No : ",self.mobile_num,"\nAddress : ",self.address)
        d.order_()
    def otp(self):
        self.a=random.randint(99999,999999)
        return self.a
    def order_(self):
        self.l=[]
        while True:
                ch=input("You want to select item y/n : ")
                if ch=='y':        
                    self.type=input("1.vegtarian\n2.non-vegetarian\n3.starters\n4.desserts\n5.icecreams\nEnter a number: ")
                    self.list=['vegtarian','non-vegetarian','starters','desserts','ice-creams']
                    if self.type in self.list:
                        d.otp()
                    self.l.append((self.type,self.a))

                else:
                    for i in range(0,len(self.l)):
                        print(self.l[i])
                    break
#order.all_types()
d=_Person_details()
#d.obj.all_types()
d.details(1,2,3)


