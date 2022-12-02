print("Advent of code - Day 2")

f = open("input.txt", "r")
file = f.read()
splitted = file.split("\n")

scores = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}

total = 0
for round in splitted:
    comb = "".join(round.split(" "))
    total = total + scores[comb]

print(total)
