import PyPDF2
obj=open('C:\\Users\\LENOVO\\Desktop\\rajiresume.pdf','rb')
obj1=PyPDF2.PdfFileReader(obj)
print(obj1.numPages)
Obj=obj1.getPage(3)
print(Obj.extractText())