print("Advent of code - Day 9")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

movement = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


head = (0, 0)
tail = (0, 0)
visited = {head}

for line in lines:
    direction, times = line.split(" ")
    times = int(times)
    for t in range(times):
        x, y = movement[direction]
        if head == tail:
            head = head[0] + x, head[1] + y
            continue
        head = head[0] + x, head[1] + y
        is_close = (abs(head[0] - tail[0]) <= 1 and abs(head[1] -
                    tail[1]) <= 1)
        if is_close == False:
            if x == 0:
                tail = head[0], tail[1] + y
            else:
                tail = tail[0] + x, head[1]
        visited.add(tail)
print(len(visited))
