prog = [1]
output = 0
step = 3
i = 0

while prog[-1] < 30:
    prog.append(prog[-1] + step)
    if 10 < prog[-1] < 30:
        output += 1

print(output)
