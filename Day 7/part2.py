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

total_disk = 70000000
total_update = 30000000

total_used = total_sizes[""]
total_unused = total_disk - total_used
total_needed = total_update - total_unused

selected_sizes = {k: v for k, v in total_sizes.items() if v >= total_needed}

min = total_disk
for s in selected_sizes:
    if selected_sizes[s] < min:
        min = selected_sizes[s]
print(min)
