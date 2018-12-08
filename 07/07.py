from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

tasks = set()
deps = defaultdict(set)

for line in lines:
    a = line[5]
    b = line[36]

    tasks.add(a)
    tasks.add(b)

    deps[b].add(a)


path = []
for task in tasks:
    path.append(min(x for x in tasks if x not in path and deps[x] <= set(path)))

print("".join(path))

order = set()
seconds = 0
counts = [0] * 5
work = [""] * 5

while True:
    for i, count in enumerate(counts):
        if count == 1:
            order.add(work[i])
        counts[i] = max(0, count - 1)

    while 0 in counts:
        i = counts.index(0)
        candidates = [x for x in tasks if deps[x] <= order]

        if not candidates:
            break

        task = min(candidates)
        tasks.remove(task)

        counts[i] = ord(task) - ord("A") + 61
        work[i] = task

    if sum(counts) == 0:
        break

    seconds += 1

print(seconds)
