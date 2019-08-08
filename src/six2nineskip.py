'''
Created on 25-Dec-2018

@author: vsrir
'''
def six2nineskip(*args):
    add = True
    total = 0  
    for num in args:
        if num == 6:
            add = False
            continue
        elif num == 9:
            add = True
            continue
        elif add:
            total = total + num
    return total

print(six2nineskip(1,6,3,9,5,6,7,8,9,0))