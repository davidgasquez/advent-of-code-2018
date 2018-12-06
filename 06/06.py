import collections

with open("input.txt") as f:
    lines = f.readlines()

coords = [(tuple(int(e) for e in coordinates.split(", "))) for coordinates in lines]

min_x = min(x for x, y in coords) - 1
max_x = max(x for x, y in coords) + 1
min_y = min(y for x, y in coords) - 1
max_y = max(y for x, y in coords) + 1

closest_points = {}

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        closest = None
        closest_num = float("inf")
        for coord_x, coord_y in coords:
            dist = abs(x - coord_x) + abs(y - coord_y)
            if dist < closest_num:
                closest_num = dist
                closest = (coord_x, coord_y)
            elif dist == closest_num:
                closest = None
        closest_points[x, y] = closest

infinite_areas = set()
for x, y in zip(range(min_x, max_x + 1), range(min_y, max_y + 1)):
    infinite_areas.add(closest_points[x, min_y])
    infinite_areas.add(closest_points[x, max_y])
    infinite_areas.add(closest_points[min_x, y])
    infinite_areas.add(closest_points[max_x, y])

areas = collections.Counter(closest_points.values())
areas.pop(None, None)

for area in infinite_areas:
    areas.pop(area, infinite_areas)

print(areas.most_common(1)[0][1])

size = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        s = sum(abs(x - coord_x) + abs(y - coord_y) for coord_x, coord_y in coords)
        if s <= 10000:
            size += 1

print(size)
