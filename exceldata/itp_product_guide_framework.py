
import xlrd
wb = xlrd.open_workbook('exceldata/itp_product_guide_framework.xls')

from itpdirectory.models import Brand

#brands
def brands():
    global wb
    sh = wb.sheet_by_index(1)
    
    for rownum in range( 1, sh.nrows):
        Brand( name=sh.row_values(rownum)[0] ).save()


brands()
