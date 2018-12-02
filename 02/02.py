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
    for idx1 in range(len(input)):
        for idx2 in range(idx1, len(input)):
            id1, id2 = input[idx1].strip(), input[idx2].strip()
            dif = 0
            for idxc in range(len(id1)):
                if id1[idxc] != id2[idxc]:
                    dif += 1
            if dif == 1:
                print(id1)
                print(id2)
                return ""


print(part_1(input))
print(part_2(input))
