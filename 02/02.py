from collections import Counter

with open("input.txt") as f:
    input = f.readlines()


def part_1(input):
    twice = 0
    thrice = 0

    for i in input:
        f = Counter(i)
        if 2 in f.values():
            twice += 1
        if 3 in f.values():
            thrice += 1

    return twice * thrice


def part_2(input):
    hasher = set()
    for line in input:
        for i, _ in enumerate(line):
            key = (line[:i], line[i + 1 :])
            if key in hasher:
                return key[0] + key[1]
            hasher.add(key)


print(part_1(input))
print(part_2(input))
