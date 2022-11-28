string = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
dictionary = {}
for i in string:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
dictionary['2'] -= 1
dictionary['9'] -= 1
summ = 0
count = 0
for i in dictionary.keys():
    if i.isdigit():
        summ += int(i) * dictionary[i]
        count += dictionary[i]
print(dictionary)
print(summ / count)