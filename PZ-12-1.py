import random

def initialize():
    array = []
    for i in range(random.randint(1, 10)):
        array.append(random.randint(-100, 100))
    return array

def findelems(a, b):
    for i in range(len(a)):
        if b.count(a[i]) == 0:
            elems.append(a[i])

a = initialize()
b = initialize()

elems = []
findelems(a, b)
findelems(b, a)

summ = sum(elems) / len(elems)

print(elems, summ)