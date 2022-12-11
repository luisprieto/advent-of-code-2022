import math


print("Advent of code - Day 11")

f = open("input.txt", "r")
file = f.read()
lines = file.split("\n\n")

monkeys = []
N_ROUNDS = 10000

for input_monkey in lines:
    monkey = {}

    _, starting_items, operation, test, test_true, test_false = input_monkey.split(
        "\n")

    monkey["items"] = starting_items.split("Starting items: ")[
        1].split(", ")
    monkey["operation"] = operation.split("Operation: ")[1]
    monkey["test_divisible_by"] = int(test.split("Test: divisible by")[1])
    monkey["test_true"] = int(test_true.split("If true: throw to monkey")[1])
    monkey["test_false"] = int(
        test_false.split("If false: throw to monkey")[1])
    monkey["n_inspections"] = 0
    monkeys.append(monkey)

divisors = []
for m in monkeys:
    divisors.append(m["test_divisible_by"])
lcm = divisors[0]
for d in divisors:
    gdc = math.gcd(lcm, d)
    lcm = (lcm * d) // gdc if gdc != 0 else (lcm * d)

for _ in range(N_ROUNDS):
    for m in monkeys:
        m["n_inspections"] += len(m["items"])

        while m["items"]:
            item = m["items"].pop(0)
            new_item = eval(m["operation"].split(
                "=")[1].replace("old", item)) % lcm
            if new_item % m["test_divisible_by"] == 0:
                monkeys[m["test_true"]]["items"].append(str(new_item))
            else:
                monkeys[m["test_false"]]["items"].append(str(new_item))

inspections = []

for m in monkeys:
    inspections.append(m['n_inspections'])
top_2 = sorted(inspections, reverse=True)[:2]
print(top_2[0] * top_2[1])
