print("Advent of code - Day 10")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

x = 1
cycle = 1
signal_strength = 0

signal_cicles = [20, 60, 100, 140, 180, 220]

for instruction in lines:
    cycle += 1
    if instruction.startswith("addx"):
        if cycle in signal_cicles:
            signal_strength += cycle * x
        x += int(instruction.split(" ")[1])
        cycle += 1
    if cycle in signal_cicles:
        signal_strength += cycle * x
print(signal_strength)
