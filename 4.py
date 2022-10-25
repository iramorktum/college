n = int(input())
summ = 0

def factorial(x):
    output = 1
    i = 1
    while i < (x + 1):
        output *= i
        i += 1
    return output

for i in range(1, n + 1):
    summ += factorial(i)

print(summ)