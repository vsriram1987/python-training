'''
Created on 29-Jul-2018

@author: vsrir
'''
stack = [1,2,3,4,5]
stack.append(6)
print(stack)
print(stack.pop())
print(stack)

from collections import deque; import datetime
i = 1
queue = []
#time taken to create list
print(datetime.datetime.now())
queue = deque(range(10000000))
print(datetime.datetime.now())
#time taken to pop
print(queue.pop())
print(datetime.datetime.now())
#time taken to pop from left
print(queue.popleft())
print(datetime.datetime.now())
