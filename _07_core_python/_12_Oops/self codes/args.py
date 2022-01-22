#Employee details retriving dynamically by using class
#Class creation
class Emp_details:
    def __init__(emp,name,id,email,age=29):
        emp.name=name=input("Enter employee name : ")
        emp.id=id=input("Enter employee id : ")
        emp.email=email=input("Enter employee email : ")
        emp.age=age
    def empdetails(emp,salary=10000):
        print('\n Name : ',emp.name,'\n ID : ',emp.id,'\n E-mail : ',emp.email,'\n Salary : ',salary,'\n Age :',emp.age)

#class calling
n=int(input("How many employees details do you want to login : "))
i=1
while i<=n:
    details=Emp_details(1,2,3)
    details.empdetails()
    i=i+1


