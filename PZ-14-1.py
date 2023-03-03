import re

hotline = open('hotline.txt', 'r')
answer = open('answer.txt', 'w')

counter = 0
thisDigits = 0

for i in hotline:
    a = re.search(r'«Горячая линия»', i)
    if a is not None:
        a = a.group(0)
        string = a + ' Министерства образования Ростовской области'
        string += i[len(a):]
        counter += 1
        answer.write(string)
    else:
        a = re.search(r'.', i)
        if a is not None:
            answer.write(i)
    phone = re.search(r'8[0-9]{8}(03|50)', i)
    if phone is not None:
        thisDigits += 1
    giaEge = re.search(r'(ГИА|ЕГЭ)', i)
    if giaEge is not None:
        phone = re.search(r'8[0-9]{9}', i)
        print(phone.group(0))

answer.close()
print(counter)
