a = int(input())
b = int(input())
c = int(input())
d = int(input())
i = 0
array = [a, b, c, d]
chet = 0

while i < 4:
    if array[i] % 2 == 0:
        chet += 1
    i += 1

print(chet)