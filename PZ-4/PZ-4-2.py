#Дано целое число N (> 0). Если оно является степенью числа 3, то вывести True, если не является - вывести False.

n = int(input())
while n > 3:
    n /= 3
if n == 3:
    print('True')
else:
    print('False')