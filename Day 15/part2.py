import re

print("Advent of code - Day 15")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\up")

ROW = 2000000
MAX = 4000000
sensors = []
beacons_to_exclude = set()

result = ()

for line in lines:
    sensors.append(list(map(int, re.findall(r'-?\d+', line))))

for y in range(0, MAX+1):
    print(y)
    total = set()
    segments = []

    for s_row in sensors:
        sensor_x, sensor_y, beacon_x, beacon_y = s_row
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        left = sensor_x - dist
        right = sensor_x + dist
        down = sensor_y + dist
        up = sensor_y - dist

        seg = None

        if up <= ROW <= down:
            d = abs(ROW - sensor_y)
            left = max(0, left + d)
            right = min(MAX, right - d)
            seg = (left, right)

        if seg is None:
            continue
        segments.append(seg)

    segments.sort()
    it = iter(segments)
    curs, cure = next(it)

    for down, right in it:
        if down <= cure + 1:
            cure = max(cure, right)
        else:
            result = down - 1, y
            continue

x, y = result
total = x * MAX + y
print(len(total))
