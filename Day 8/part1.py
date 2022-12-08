print("Advent of code - Day 8")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

height = len(lines)
width = len(lines[0])

visible = height * 2 + width * 2 - 4

for i in range(len(lines)):
    line = lines[i]
    if i == 0 or i == height - 1:
        continue

    for j in range(len(line)):
        tree = line[j]
        if j == 0 or j == width - 1:
            continue

        right = (tree > t for t in line[j + 1:])
        up = (tree > lines[k][j] for k in range(i - 1, -1, -1))
        down = (tree > lines[k][j] for k in range(i + 1, len(lines)))
        left = (tree > t for t in line[:j])

        if all(up) or all(down) or all(left) or all(right):
            visible += 1

print(visible)
