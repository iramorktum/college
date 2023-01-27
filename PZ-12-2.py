import string
text = 'TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longland 481 feet (147 metres) high.'

digits = ''
for i in text:
    if i.isdigit():
        digits += i

print(digits)

digits = ''
for i in text:
    if i in string.digits:
        digits += i

print(digits)