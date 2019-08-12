import timeit
def mult1(val):
    return str(val << 2)
def mult2(val):
    return str(val*4)
print(timeit.timeit("-".join(map(mult1,range(100))),number=1000000))

print(timeit.timeit("-".join(map(mult2,range(100))),number=1000000))
