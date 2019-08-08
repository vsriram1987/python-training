'''
Created on 12-Dec-2018

@author: vsrir
'''
text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = 0
new_text = ''
for i in range(len(text)):
    if alphabet.find(text[i]) >= 0 :
        if alphabet.find(text[i]) + 2 > len(alphabet) - 1 :
            new_text += alphabet[alphabet.find(text[i]) - len(alphabet) + 2]
        else:
            print(alphabet.find(text[i]))
            new_text += alphabet[alphabet.find(text[i]) + 2]
    else:
        new_text += text[i]
print(new_text)