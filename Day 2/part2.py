print("Advent of code - Day 2")

f = open("input.txt", "r")
file = f.read()
splitted = file.split("\n")

scores = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}

total = 0
for round in splitted:
    comb = "".join(round.split(" "))
    total = total + scores[comb]

print(total)
