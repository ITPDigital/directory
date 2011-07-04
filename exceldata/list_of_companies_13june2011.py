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



wb = xlrd.open_workbook('list_of_companies_13june2011.xls')

mi_sh = wb.sheet_by_index( 2 )

PERSON_JOB_FUNCTION = ()

for rownum in range(mi_sh.nrows):
    PERSON_JOB_FUNCTION = PERSON_JOB_FUNCTION + ((rownum + 1, mi_sh.row_values(rownum)[0]),)




pprint.pprint( PERSON_JOB_FUNCTION   )  
