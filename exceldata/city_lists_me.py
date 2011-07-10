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



wb = xlrd.open_workbook('city_lists_me.xls')

sh = wb.sheet_by_index(0)

CITIES = ()
COUNTRIES_CITIES_MAP = {}


cities_map = []
for rownum in range(2,sh.nrows):
    CITIES = CITIES + ((rownum-1,sh.row_values(rownum)[0]),)
    cities_map.append( rownum-1 )

COUNTRIES_CITIES_MAP.update({ u'SA' : cities_map } )

next = rownum

cities_map = []
for rownum in range(2,10):
    CITIES = CITIES + (( next+rownum-2,sh.row_values(rownum)[3]),)
    cities_map.append( rownum + next-2 )

COUNTRIES_CITIES_MAP.update({ u'AE' : cities_map } )

next = rownum + next

cities_map = []
for rownum in range(2,8):
    CITIES = CITIES + (( next+rownum-3,sh.row_values(rownum)[6]),)
    cities_map.append( rownum + next-3 )

COUNTRIES_CITIES_MAP.update({ u'OM' : cities_map } )


pprint.pprint( CITIES )  
print ( COUNTRIES_CITIES_MAP )  
