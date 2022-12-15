#!/usr/bin/env python3

import json


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if (isinstance(a, int) and not isinstance(b, int)) or (not isinstance(a, int) and isinstance(b, int)):
        if isinstance(a, int):
            return compare([a], b)
        else:
            return compare(a, [b])

    for x, y in zip(a, b):
        res = compare(x, y)
        if res != 0:
            return res

    return len(a) - len(b)


print("Advent of code - Day 13")

f = open("input.txt", "r")
file = f.read().replace('\n\n', '\n')
lines = file.split("\n")

packets = []
for line in lines:
    packets.append(json.loads(line))

pairs = []
for i in range(0, len(packets), 2):
    pairs.append(packets[i:i + 2])

compare_values = []
for i, pair in enumerate(pairs):
    if compare(*pair) < 0:
        compare_values.append(i+1)
result = sum(compare_values)


print(result)
