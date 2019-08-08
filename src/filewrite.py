'''
Created on 29-Jul-2018

@author: vsrir
'''
import os
un = "Enter whatever the hell you want"
print(os.getcwd())
os.chdir("C:/users/vsrir/desktop")
print(os.getcwd())
if os.path.exists("C:/testfile.txt"):
    print("path found")
else:
    print("path invalid")
file = open("C:/users/vsrir/desktop/testfile.txt", "w")
i = 0
for i in range(len(un)):
    file.write(un[i] + "\n")
    i = i + 1
file.write("--end of file--")
file.close()
file = open("C:/users/vsrir/desktop/testfile.txt", "r")
print(file.read().replace('\n','\\n'))
file.seek(0)
print(file.readlines())
file.close()
with open("C:/users/vsrir/desktop/testfile.txt", "a") as file:
    file.write("\nMore text at the end...")
with open("C:/users/vsrir/desktop/testfile.txt", "r") as file:
    print(file.read())
