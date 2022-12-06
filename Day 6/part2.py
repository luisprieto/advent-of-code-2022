print("Advent of code - Day 6")

f = open("input.txt", "r")
file = f.read()

first_marker = -1

for i in range(0, len(file)-4):
    current_marker = i+4
    chars = set(file[i:current_marker])
    if len(chars) == 4:
        first_marker = current_marker
        break

marker = -1

for i in range(first_marker, len(file)-14):
    current_marker = i+14
    chars = set(file[i:current_marker])
    if len(chars) == 14:
        marker = current_marker
        break
print(marker)
