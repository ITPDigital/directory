import xlrd
import pprint


def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    try:
        return [k for k, v in dic.iteritems() if v == val][0]
    except:
        print "could not be found >> %s \n" % val
 

def find_value(dic, key):
    """return the value of dictionary dic given the key"""
    return dic[key]


class Lookup(dict):
    """
    a dictionary which can lookup value by key, or keys by value
    """
    def __init__(self, items=[]):
        """items can be a list of pair_lists or a dictionary"""
        dict.__init__(self, items)
 
    def get_key(self, value):
        """find the key(s) as a list given a value"""
        return [item[0] for item in self.items() if item[1] == value]
 
    def get_value(self, key):
        """find the value given a key"""
        return self[key]



wb = xlrd.open_workbook('itp_industry_list.xls')

mi_sh = wb.sheet_by_index(0)
sp_sh = wb.sheet_by_index(1)

MAIN_INDUSTRY = ()
SPECIFIC_INDUSTRY = ()
MAIN_SPECIFIC_MAP = {}

for rownum in range(mi_sh.nrows):
    MAIN_INDUSTRY = MAIN_INDUSTRY + ((rownum, mi_sh.row_values(rownum)[0]),)


mi_dict = dict (MAIN_INDUSTRY)

for rownum in range(sp_sh.nrows):
    SPECIFIC_INDUSTRY = SPECIFIC_INDUSTRY + ( (rownum, sp_sh.row_values(rownum)[2] ),  )
    try:
        MAIN_SPECIFIC_MAP[ find_key( mi_dict, sp_sh.row_values(rownum)[1]) ].append( rownum  )
    except:   
        MAIN_SPECIFIC_MAP.update( { find_key( mi_dict, sp_sh.row_values(rownum)[1]) : [ rownum ] } )   


pprint.pprint( MAIN_INDUSTRY )  
pprint.pprint( SPECIFIC_INDUSTRY )  
print MAIN_SPECIFIC_MAP 
