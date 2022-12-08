print("Advent of code - Day 8")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

height = len(lines)
width = len(lines[0])

count = 0

for i in range(len(lines)):
    line = lines[i]
    if i == 0 or i == height - 1:
        continue

    for j in range(len(line)):
        tree = line[j]
        if j == 0 or j == width - 1:
            continue

        for right in range(j + 1, width):
            if line[right] >= tree:
                break

        for left in range(j - 1, -1, -1):
            if line[left] >= tree:
                break

        for down in range(i + 1, height):
            if lines[down][j] >= tree:
                break

        for up in range(i - 1, -1, -1):
            if lines[up][j] >= tree:
                break

        score = (right - j) * (j - left) * (down - i) * (i - up)

        if score > count:
            count = score

print(count)
