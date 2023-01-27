import random

matrix = []

for i in range(3):
    help = []
    for j in range(3):
        help.append(random.randint(-100, 100))
    matrix.append(help)

small = min(matrix[1])
print(matrix, small)
