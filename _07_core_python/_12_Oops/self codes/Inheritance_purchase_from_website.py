#Online shopping website using Inheritance
class Other:
    def no_service(self):
        print("Sorry!!!")
        print("We are not giving service now....\nThanks for choosing our website...")
class Other1(Other):
    def service(self):
        print("Yes,We have that product....")
    def serviced_products(self,a):
        self.a=a
        print("These {} are available in our website....".format(m[0][self.a-1]))
        for i in range(0,len(m[self.a])):
            print("\t{}.{}".format(i+1,m[self.a][i]))
        print("You can buy from our website....\nThanks for choosing our website...")
class Category(Other1):    
    def __init__(self):
        pass
    def item(self,m,n):
        print('Products in our website : ')
        for i in range(0,len(m[0])):
            print('\t',i+1,'.',m[0][i])
        prdt=Other1()
        self.n=n
        self.n=int(input('\nEnter s.no of a product : '))
        if self.n  in [1,2,3,4]:
            prdt.service()
            prdt.serviced_products(self.n)
        else:
            prdt.no_service()
#MAIN PROGRAM
m=[['Kitchen Items','Clothing Category','Electronic Goods','HomeAppliances'],['Chimneys','Induction Stoves','Microwave Ovens',"Kitchen Storage Items"],["Men's Wear","Women's Wear","Kid's Wear"],['Laptops','Mobiles','tablets','Cameras'],['Television Sets','Air Conditioners','Geazers']]
site=input("Please enter a website : ")
product=Category()
product.item(m,None)