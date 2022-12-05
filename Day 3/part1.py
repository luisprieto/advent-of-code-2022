def get_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


print("Advent of code - Day 3")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

total = 0

for line in lines:
    first = set(line[:len(line) // 2])
    last = set(line[len(line) // 2:])
    common = next(iter(first.intersection(last)))
    total = total + get_priority(common)
print(total)
