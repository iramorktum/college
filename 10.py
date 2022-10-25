n = int(input()) - 3
first = [0, 1, 1]
i = 0

while i < n:
    first.append(first[-1] + first[-2])
    i += 1

print(first)