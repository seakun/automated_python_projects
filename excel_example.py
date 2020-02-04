import openpyxl, import os

os.chdir(example.xlsx)

workbook = openpyxl.load_workbook('example.xlsx')
workbook.get_sheet_by_name('Sheet1')

workbook.get_sheet_names()

cell = sheet['A1']
cell.value

str(sheet['A1'].value)

sheet.cell(row=1, column=2)
# starts at 1, not 0

for i in range(1, 8):
    print(i, sheet.ceel(row=i, column=2).value)
