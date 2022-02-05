#POLYMORPHISM by using method overriding and overloading
class Poly:
    def __init__(self):
        pass
    def area1(self,b,h):
        self.b=b
        self.h=h
        print("Area of triangle is {}".format(0.5*self.b*self.h))
    def area(self,a):
        self.a=a
        print("Area of square is {}".format(self.a*self.a))

class Poly2:
    def __init__(self):
        pass
    def area(self,a):
        aa=self.a+self.a
        print("Area from second base class",aa)

class Poly1(Poly,Poly2):
    def __init__(self):
        pass
    def area1(self,a,b):#method overriding
        super().area1(a,b)
        self.a=a
        self.b=b
        print("Area of rectangle is {}".format(a*b))
    def area(self,a):#method overriding
        super().area(a)
        self.a=a
        print("Area of circle is {}".format((22/7)*self.a*self.a))
    def product(self,*a):#method overloading
        vol=1
        for x in a:
            vol=vol*x
        print('Product is ',vol)


a=Poly1()
a.area(12)
a.area1(10,12)
a.product(1,2,3)
a.product(3,4,5,6,7)