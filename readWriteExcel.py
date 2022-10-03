import xlsxwriter

def write2Excel():
    workbook = xlsxwriter.Workbook('c:/Users/User/Desktop/testdata.xlsx')
    worksheet = workbook.add_worksheet('test')
    worksheet.write('A1', 'Hello')
    worksheet.write('A2', 'Hello')
    worksheet.write('A3', 'Hello')
    worksheet.write('A4', 'Hello')
    worksheet.write('A5', 'Hello')
    worksheet.write('A6', 'Hello')
    worksheet.write('A7', 'Hello')
    worksheet.write('A8', 'Hello')
    worksheet.write('A9', 'Hello')


    workbook.close()