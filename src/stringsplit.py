'''
Created on 25-Dec-2018

@author: vsrir
'''
str = "Print every word starting with s in this sentence"
strarray = str.split(" ")
print(strarray)
for word in strarray:
    if len(word)%2 == 0:
        print(word)