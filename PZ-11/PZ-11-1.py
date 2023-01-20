a = '1 -4 5 6'
b = '-4 -1 7 9'

inta = list(map(int, a.split(' ')))
intb = list(map(int, b.split(' ')))

neg = []
for i in range(len(inta)):
    if inta[i] < 0:
        neg.append(inta[i])
negcount = len(neg)
aver = sum(neg) / negcount

pos = []
for i in range(len(intb)):
    if intb[i] < 0:
        pos.append(intb[i])
poscount = len(pos)
possum = sum(pos)

