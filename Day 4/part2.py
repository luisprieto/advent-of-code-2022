print("Advent of code - Day 4")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

count = 0

for line in lines:
    pair_a, pair_b = line.split(",")
    s_a1, s_a2 = pair_a.split("-")
    s_b1, s_b2 = pair_b.split("-")

    a1 = int(s_a1)
    a2 = int(s_a2)
    b1 = int(s_b1)
    b2 = int(s_b2)

    mx = max(a1, b1)
    mn = min(a2, b2)

    if mx <= mn:
        count += 1

print(count)
