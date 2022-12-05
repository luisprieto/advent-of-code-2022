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

for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    common = set()
    for ch in group[0]:
        if ch in group[1] and ch in group[2]:
            total = total + get_priority(ch)
            break
print(total)
