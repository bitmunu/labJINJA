import openpyxl
import docxtpl

wb = openpyxl.load_workbook("Ученики.xlsx")
ws = wb.active

temp = []
for x in ws.values:
    temp.append(x)
print(temp)
temp.pop(0)
doc = docxtpl.DocxTemplate("hehe.docx")
env = {"values":temp}

doc.render(env)
doc.save("награды.docx")
