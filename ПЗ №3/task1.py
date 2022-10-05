n = list(input())

output = n[0] != n[1] and n[1] != n[2] and n[2] != n[0]

if output == True:
    print('Высказывание верно')
else:
    print('Высказывание ложно')
