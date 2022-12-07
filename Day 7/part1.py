print("Advent of code - Day 7")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

sizes = {}
current = []
redundancy = ""

for command in lines:
    if command.startswith("$"):
        splitted = command.split(" ")
        splitted.pop(0)
        if splitted[0] == "cd":
            if splitted[1] == "..":
                current.pop()
            else:
                current.append(splitted[1])
    else:
        splitted = command.split(" ")
        if splitted[0] != "dir" and splitted[0] != "":
            if not tuple(current) in sizes:
                sizes[tuple(current)] = 0
            sizes[tuple(current)] += int(splitted[0])


total_sizes = {}
for s in sizes.keys():
    current_path = ""
    for dir in s:
        if dir != "/":
            current_path += "/" + dir
        if current_path not in total_sizes:
            total_sizes[current_path] = 0
        total_sizes[current_path] += sizes[s]

selected_sizes = {k: v for k, v in total_sizes.items() if v <= 100000}
count = 0
for s in selected_sizes:
    count += selected_sizes[s]
print(count)
