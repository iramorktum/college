#Дано трёхзначное число. Проверить истиинность высказывания: "Все цифры данного числа различны".

n = list(input())
if n[0] != n[1] and n[1] != n[2] and n[0] != n[2]:
    print('True')
else:
    print('False')