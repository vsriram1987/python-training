'''
Created on 25-Dec-2018

@author: vsrir
'''
def check_right_angle(a,b,c,num):
    if a+b+c == num:
        if a**2 + b**2 == c**2:
            return [a,b,c]
        else:
            return []
    else:
        return []

def count_right_triangles(num):
    count = 0
    for i in range(1, int(num / 2)):
        for j in range(i, int(num / 2)):
            for k in range(j, int(num / 2)):
                if len(check_right_angle(i,j,k,num)) > 0:
                    #count += 1
                    print(check_right_angle(i,j,k,num))
    return count

count_right_triangles(840)
'''
max_i = [0,0]
for i in range(5,1000):
    j = count_right_triangles(i)
    if j > max_i[1]:
        max_i[0]=i
        max_i[1]=j
        print(max_i)'''