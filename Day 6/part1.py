print("Advent of code - Day 6")

f = open("input.txt", "r")
file = f.read()

marker = -1

for i in range(0, len(file)-4):
    current_marker = i+4
    chars = set(file[i:current_marker])
    if len(chars) == 4:
        marker = current_marker
        break

print(marker)
