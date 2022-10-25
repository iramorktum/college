n = int(input())
prog = [1]
i = 1

while i <= n:
    prog.append(prog[-1] + 3)
    i += 1

i = 0
while i <= n:
    prog[i] = round(prog[i] / 2)
    i += 1

print(prog)