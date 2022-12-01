print("Advent of code - Day 1")

f = open("input.txt", "r")
file = f.read()
splitted = file.split("\n\n")

elves = []

for el in splitted:
    elf = el.split("\n")
    count = 0
    for cal in elf:
        count += int(cal)
    elves.append(count)
elves.sort(reverse=True)

topThree = elves[0:3]
print(sum(topThree))
