a = int(input())
b = int(input())
c = int(input())
d = int(input())
i = 0
minus = 0
array = [a, b, c, d]

while i < 4:
    if array[i] < 0:
        minus += 1
    i += 1

print(sum(array))
print(minus)