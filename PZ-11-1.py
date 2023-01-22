import random

numbers = [[], []]
for i in range(2):
    for j in range(random.randint(2, 10)):
        numbers[i].append(random.randint(-100, 100))
    numbers[i] = list(map(str, numbers[i]))

first = open('first.txt', 'w')
last = open('last.txt', 'w')

first.write(' '.join(numbers[0]))
last.write(' '.join(numbers[1]))

first.close()
last.close()

infofirst =  ' '.join(numbers[0])
infolast = ' '.join(numbers[1])

neg = []
for i in range(len(numbers[0])):
    if int(numbers[0][i]) < 0:
        neg.append(numbers[0][i])
negcount = len(neg)
numbers[0] = list(map(int, numbers[0]))
average = sum(numbers[0]) / len(numbers[0])

pos = []
for i in range(len(numbers[1])):
    if int(numbers[1][i]) > 0:
        pos.append(numbers[1][i])
pos = list(map(int, pos))
poscount = len(pos)
summ = sum(pos)

output = open('output.txt', 'w')

output.write('Содержимое первого файла: ' + ' '.join(list(map(str, numbers[0]))) + '\n')
output.write('Отрицательные элементы: ' + ' '.join(neg) + '\n')
output.write('Количество отрицательных элементов: ' + str(negcount) + '\n')
output.write('Среднее арифметическое: ' + str(average) + '\n\n')
output.write('Содержимое второго файла: ' + ' '.join(list(map(str, numbers[1]))) + '\n')
output.write('Положительные элементы: ' + ' '.join(list(map(str, pos))) + '\n')
output.write('Количество положительных элементов: ' + str(poscount) + '\n')
output.write('Сумма положительных  элементов: ' + str(summ) + '\n')

output.close()
