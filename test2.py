import xlsxwriter

Wb = xlsxwriter.Workbook('arrays' + str(1) +'.xlsx')
Ws = Wb.add_worksheet()

array = [['a1', 'a2', 'a3'],
         ['a4', 'a5', 'a6'],
         ['a7', 'a8', 'a9'],
         ['a10', 'a11', 'a12', 'a13', 'a14']]

row = len(array)


for row in range(row):
    Ws.write_row(row, 0, array[row])


Wb.close()


# a = ['a1', 'a2', 'a3']
# b = ['a4', 'a5', 'a6']
# c = ['a10', 'a11', 'a12', 'a13', 'a14']
# arr = []
#
#
# for i in range(3):
#     arr.append(a)
#
# print(arr)