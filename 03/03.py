import numpy as np

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

dim = 1024
matrix = np.zeros((dim, dim))

# Fill the matrix
for line in lines:
    id, _, pos, size = line.split(" ")
    row, col = (int(x) for x in pos[:-1].split(","))
    w, h = [int(x) for x in size.split("x")]

    matrix[row : row + w, col : col + h] += 1


part_1 = (matrix > 1).sum()


for line in lines:
    id, _, pos, size = line.split(" ")

    row, col = (int(x) for x in pos[:-1].split(","))
    w, h = [int(x) for x in size.split("x")]

    # All values inside the matrix should be 1 (width * height)
    if matrix[row : row + w, col : col + h].sum() == w * h:
        part_2 = id

print(part_1)
print(part_2)
