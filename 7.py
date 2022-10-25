n = int(input('Количество чисел: '))
numbers = []
output = 0
i = 0

while i < n:
    num = int(input())
    numbers.append(num)
    if num == 0:
        output += 1
    i += 1

print(output)
