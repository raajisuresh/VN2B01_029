from xml.dom import XMLNS_NAMESPACE

import openpyxl
path='C:\\Users\\LENOVO\\Desktop\\029_EAF_Rajeswari.B.xls'

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row = 1, column = 1)
print(cell_obj.value)