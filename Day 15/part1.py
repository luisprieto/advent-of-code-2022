import re

print("Advent of code - Day 15")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n")

ROW = 2000000

sensors = []
beacons_to_exclude = set()
total = set()

for line in lines:
    sensors.append(list(map(int, re.findall(r'-?\d+', line))))

for s_row in sensors:
    sensor_x, sensor_y, beacon_x, beacon_y = s_row

    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    left = sensor_x - dist
    right = sensor_x + dist
    down = sensor_y + dist
    up = sensor_y - dist

    if up <= ROW <= down:
        d = abs(ROW - sensor_y)
        a = left + d
        b = right - d
        if a > b:
            numbers = range(a, b - 1, -1)
        else:
            numbers = range(a, b + 1, 1)
        rang = list(numbers)
        total.update(rang)
    if beacon_y == ROW:
        beacons_to_exclude.add(beacon_x)

total = total - beacons_to_exclude
print(len(total))
