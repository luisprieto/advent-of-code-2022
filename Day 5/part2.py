print("Advent of code - Day 5")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

start = []
stacks = [None]
moves = []

lines_flag = False

for line in lines:
    if (line == ""):
        lines_flag = True
    elif (lines_flag == True):
        m = line.split()
        moves.append((int(m[1]), int(m[3]), int(m[5])))
    else:
        start.append(line)

for i, el in enumerate(zip(*start)):
    if i % 4 == 1:
        stack = ''.join(el[:-1]).lstrip()
        stacks.append(stack)

for move, frm, to in moves:
    to_move = stacks[frm][:move]
    to_keep = stacks[frm][move:]

    stacks[frm] = to_keep
    stacks[to] = to_move + stacks[to]

result = ''.join(s[0] for s in stacks[1:])

print(result)
