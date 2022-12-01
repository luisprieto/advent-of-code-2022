print("Advent of code - Day 1")

f = open("input.txt", "r")
file = f.read()
splitted = file.split("\n\n")

max = 0

for el in splitted:
    elf = el.split("\n")
    count = 0
    for cal in elf:
        count += int(cal)
    if count > max:
        max = count
print(max)
