a = int(input())
b = int(input())
c = int(input())

d = 0
e = 0

output = 0

while a > 0:
    if a - c >= 0:
        d += 1
    a -= c

while b > 0:
    if b - c >= 0:
        e += 1
    b -= c

i = 0
while i < d:
    output += e
    i += 1

print(output)

