n, k, l = int(input('Количество элементов: ')), int(input('Не считать от: ')) - 1, int(input('До: ')) - 1
array = []
output = 0

for i in range(n):
    array.append(int(input('Введите элемент: ')))

for i in range(n):
    if k > i or i > l:
        output += array[i]

print(output)
