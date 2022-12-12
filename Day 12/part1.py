from collections import deque
print("Advent of code - Day 11")


def get_neighbors(matrix, pos):
    x, y = pos
    max = matrix[x][y] + 1

    height = len(matrix)
    width = len(matrix[0])

    neighbors = []

    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= nx < height and 0 <= ny < width:
            neighbors.append((nx, ny))

    res = []
    for nx, ny in neighbors:
        if matrix[nx][ny] <= max:
            res.append((nx, ny))
    return res


def bfs(matrix, start, end):
    visited = set()
    queue = deque()
    queue.append([0, start])

    while queue:
        dist, pos = queue.popleft()
        x, y = pos

        if pos == end:
            return dist

        if pos not in visited:
            visited.add(pos)

            for neighbor in get_neighbors(matrix, pos):
                if neighbor in visited:
                    continue
                queue.append((dist + 1, neighbor))

    return None


f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

START_CHAR = "S"
END_CHAR = "E"

MIN_CHAR = 'a'
MAX_CHAR = 'z'

start = None
end = None

matrix = []

for i, line in enumerate(lines):
    row = []
    for j, char in enumerate(line):
        if char == START_CHAR:
            start = i, j
            row.append(ord(MIN_CHAR))
        elif char == END_CHAR:
            end = i, j
            row.append(ord(MAX_CHAR))
        else:
            row.append(ord(char))
    matrix.append(row)
print(bfs(matrix, start, end))
