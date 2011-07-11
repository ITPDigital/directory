"""
== Before Running 
Add year: 2011
Directory for each excel and add the id to the map
"""
from itpdirectory.models import Category, Directory
import xlrd


path = "exceldata/directory/"

items = [
    { 'excel' : 'construction_contractors_dir_index_2011.xls' , 'id' : 3 },
    { 'excel' : 'construction_design_dir_index_2011.xls' , 'id' : 4 },
    { 'excel' : 'oil_gas_dir_index_2011.xls' , 'id' : 5 },
    { 'excel' : 'utilities_dir_index_2011.xls' , 'id' : 6 },
    { 'excel' : 'hospitality_catering_dir_index_2011.xls' , 'id' : 7 },
    { 'excel' : 'supply_chain_dir_index_2011.xls' , 'id' : 8 },
    { 'excel' : 'it_product_guide_framework_v4.xls' , 'id' : 9 },
]

items = [
    { 'excel' : 'it_product_guide_framework_v4.xls' , 'id' : 9 },
]


for item in items:
    wb = xlrd.open_workbook( "%s%s" % ( path, item['excel']) )
    sh = wb.sheet_by_index(0)
    directory = Directory.objects.get(pk=item['id'] )
    parents = []
    nrows = sh.nrows
    ncols = sh.ncols
    for rownum in range(sh.nrows):
        if rownum == 0:
            for parent in sh.row_values(rownum):
                parent_obj = Category( name= parent, directory=directory )
                parent_obj.save()
                parents.append( parent_obj )
                
        for colnum in range(sh.ncols):
            val = sh.row_values(rownum)[colnum]
            if val != "": 
                print parents[colnum], val
                Category( name=val, directory=directory, category=parents[colnum] ).save()
