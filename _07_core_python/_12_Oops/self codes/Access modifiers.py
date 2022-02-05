#Data ENCAPSULATION by using Access modifiers
class ProtectedAccessModifiers():
    def __init__(self):
        pass
    def public(self,a):#public method
        self.name=a
        print("name is ",self.name,'From public method')
    def _protected(self,location):#protected method
        self._location=location
        print("Location is ",self._location,'From protected method')
    def age(self,b):#public method
        self.b=b
        print("Age is ",self.b,'From public method')
    def __age(__b):#private method
        print("Age is ",__b,"From private method")
    __age(33)
    
s=ProtectedAccessModifiers()
s.age(23)


class PrivateAccessModifiers(ProtectedAccessModifiers):
    def public1(self,a):
        self.a=a
        print('a is ',self.a,'From public method')
    def all(self):
        ab=ProtectedAccessModifiers()
        ab.public('yash')
        ab._protected('chennai')
        #ab.__age(25)
class exp:
    def exper(self):
        a=ProtectedAccessModifiers()
        a.public('yash')

z=exp()
z.exper()
#z._protected('ooty')

a=ProtectedAccessModifiers()
a.public('honey')
a._protected('ndl')         #protected method
#a.__age(23)                 #private method

raji=PrivateAccessModifiers()
raji.public1(5)  
raji.all()              #protected method by inheritance
#raji._protected('delhi')
#raji.__age()              #Private method
#raji._protected('hyd')