n = int(input('Количество точек: '))
xs, ys = [], []
low = [0, 0]

for i in range(n):
    xs.append(int(input('X ' + str(i + 1) + '-ой точки: ')))
    ys.append(int(input('Y ' + str(i + 1) + '-ой точки: ')))

x, y = int(input('X B: ')), int(input('Y B: '))

for i in range(n):
    r = ((xs[i] - x) ** 2 + (ys[i] - y) ** 2) ** 0.5
    if i == 0 or r < low[1]:
        low[0] = i
        low[1] = r

print(str(xs[low[0]]) + '; ' + str(ys[low[0]]))

