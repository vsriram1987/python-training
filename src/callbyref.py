'''
Created on 29-Jul-2018

@author: vsrir
'''
i = 2
j = ['1','2','b']
def testfn(i,j=[],val=""):
    '''Tests passing by ref vs passing by value'''
    i = i + 1
    if val!="":
        j.extend(j)
        j.append(val)
testfn(i,j,'d')
print(i)
print(j)
print(testfn.__doc__)