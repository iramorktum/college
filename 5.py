n = int(input('Количество чисел: '))
numbers = []
i = 0

while i < n:
    numbers.append(int(input()))
    i += 1

print(sum(numbers) / len(numbers))