n = int(input('Количество элементов: '))
array = []
output = True

for i in range(n):
    array.append(int(input('Введите элемент: ')))

for i in range(n):
    if array.count(array[i]) > 1 or array[i] < 1 or n < array[i]:
        output = False
        print(i)
        break

if output:
    print(0)
