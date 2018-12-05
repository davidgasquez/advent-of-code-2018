from functools import reduce
import string

with open("input.txt", "r") as f:
    polymer = f.readline().strip()


def react(polymer):
    return reduce(lambda x, y: x[1:] if x and x[0] != y and x[0].upper() == y[0].upper() else y + x, reversed(polymer))


part_1 = len(react(polymer))
part_2 = min((len(react(polymer.replace(r, "").replace(r.lower(), ""))) for r in string.ascii_uppercase))

print(part_1)
print(part_2)
