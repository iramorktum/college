a = list(input('Строка: '))

for i in range(len(a)):
    if a[i] == ' ':
        a[i] = '.'

print(''.join(a))
