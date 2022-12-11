print("Advent of code - Day 10")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

x = 1
cycle = 1
signal_strength = 0
crt = []
row = ''

signal_cicles = [20, 60, 100, 140, 180, 220]

CRT_WIDTH = 40
PIXEL_WIDTH = 3

for instruction in lines:
    row += '#' if x <= cycle % CRT_WIDTH < x + PIXEL_WIDTH else ' '
    cycle += 1
    if instruction.startswith("addx"):
        if cycle in signal_cicles:
            signal_strength += cycle * x
        elif cycle % CRT_WIDTH == 1:
            crt.append(row)
            row = ''
        row += '#' if x <= cycle % CRT_WIDTH < x + PIXEL_WIDTH else ' '
        x += int(instruction.split(" ")[1])
        cycle += 1
    if cycle in signal_cicles:
        signal_strength += cycle * x
    elif cycle % CRT_WIDTH == 1:
        crt.append(row)
        row = ''
print('\n'.join(crt))
