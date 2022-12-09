print("Advent of code - Day 9")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

movement = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


knots = [(0, 0)] * 10
visited = {knots[0]}

for line in lines:
    direction, times = line.split(" ")
    times = int(times)
    for t in range(times):
        x, y = movement[direction]
        knots[0] = knots[0][0] + x, knots[0][1] + y
        for i in range(9):
            if (knots[i][0] - knots[i + 1][0])**2 + (knots[i][1] - knots[i + 1][1])**2 >= 4:
                inc_x = 1 if knots[i][0] - knots[i + 1][0] > 0 else - \
                    1 if knots[i][0] - knots[i + 1][0] < 0 else 0
                inc_y = 1 if knots[i][1] - knots[i + 1][1] > 0 else - \
                    1 if knots[i][1] - knots[i + 1][1] < 0 else 0
                knots[i + 1] = knots[i + 1][0] + inc_x, knots[i + 1][1] + inc_y
        visited.add(knots[9])
print(visited)
print(len(visited))
