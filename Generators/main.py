import sys

def myGenerator(n):
    for x in range(n):
        yield x ** 3

values = myGenerator(3)

print(sys.getsizeof(values))