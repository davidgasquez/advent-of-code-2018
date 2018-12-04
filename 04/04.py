import re
import numpy as np
from collections import defaultdict
from functools import partial

with open("input.txt", "r") as f:
    records = f.readlines()

records = sorted(records)

current_guard_id = None
guards = defaultdict(partial(np.zeros, 60))

for record in records:
    minute = int(record[15:17])
    if "begins shift" in record:
        current_guard_id = int(re.match(r".* #(\d+) .*", record).group(1))
    elif "falls asleep" in record:
        sleep_start = minute
    else:
        sleep_end = minute
        guards[current_guard_id][sleep_start:sleep_end] += 1

part_1_guard = max([(np.sum(minutes), guard) for guard, minutes in guards.items()])[1]
part_1_minute = np.argmax(guards[part_1_guard])

print(part_1_guard * part_1_minute)

part_2_guard = max(
    [(np.max(guards[guard]), guard) for guard, minutes in guards.items()]
)[1]
part_2_minute = np.argmax(guards[part_2_guard])

print(part_2_guard * part_2_minute)
