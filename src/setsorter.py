'''
Created on 06-Jan-2019

@author: vsrir
'''
import string
from _sre import ascii_tolower
def checkalph(stringval):
    varset = ""
    #list will convert set to list
    #set will take unique values in map
    #map has a lambda to convert all characters to lower case
    #the list passed to the map is a filter
    #filter has a lambda to only take characters and ignore everything else from the input string
    varlist = list(set(map(lambda str:str.lower(),filter(lambda a:a in string.ascii_lowercase + string.ascii_uppercase,stringval))))
    #then sort the alphabets and convert to string
    varlist.sort()
    varset = "".join(varlist)
    alphset = string.ascii_lowercase
    #now do the comparison and return true or false
    print(varset)
    print(alphset)
    if varset == alphset.lower():
        return True
    return False

print(checkalph("the quicKest #superquick Brown coloured fox jumped over the lazy dogs yet did not Succeed!!!"))
    