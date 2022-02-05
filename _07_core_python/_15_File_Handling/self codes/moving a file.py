#Changing path of a file
try :
    import os
    #os.rename('present path','desired path')
    os.rename('C:\\Users\\LENOVO\\Desktop\\raji resume.docx','C:\\Users\\LENOVO\\Desktop\\raji ressumes\\raji_resume1.docx')
except FileNotFoundError:
    print("This file is not existed..")