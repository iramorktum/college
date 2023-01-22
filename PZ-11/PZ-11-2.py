text = open('text.txt')

signs = 0
reverse = []
for i in text:
    for j in range(len(i)):
        if i[j] == '.' or i[j] == ',' or i[j] == '!':
            signs += 1
    reverse.insert(0, i)
    print(i)

print('\n\n')
print('Количество знаков препинания: ' + str(signs))

rev = open('reverse.txt', 'w')
for i in range(len(reverse)):
    rev.write(reverse[i] + '\n' * int(i == 0))

rev.close()
    
