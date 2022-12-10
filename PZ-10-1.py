import random

fish = ['стерлядь', 'окунь', 'сом', 'лосось', 'мойва']
fishButOther = {'стерлядь', 'окунь', 'сом', 'лосось', 'мойва'}
first = set()
second = set()
third = set()
for i in range(random.randint(1, 3)):
    first.add(fish[random.randint(0, 4)])
for i in range(random.randint(1, 3)):
    second.add(fish[random.randint(0, 4)])
for i in range(random.randint(1, 3)):
    third.add(fish[random.randint(0, 4)])
allFish = first | second | third
diff = fishButOther.difference(allFish)

if diff == set():
    print(allFish, {})
else:
    print(allFish, diff)



