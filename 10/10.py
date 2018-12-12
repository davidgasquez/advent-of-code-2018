import numpy as np
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

data = np.array([[int(i) for i in re.findall(r"-?\d+", line)] for line in lines])

X, Y, A = [], [], []
for i in range(20000):
    X.append((data[:, 0] + i * data[:, 2]).max() - (data[:, 0] + i * data[:, 2]).min())
    Y.append((data[:, 1] + i * data[:, 3]).max() - (data[:, 1] + i * data[:, 3]).min())
    A.append(X[i] * Y[i])

t = A.index(min(A))

lx = X[t] + 1
ly = Y[t] + 1

data[:, :2] += t * data[:, 2:]
data[:, 0] -= data[:, 0].min()
data[:, 1] -= data[:, 1].min()

canvas = np.zeros((ly, lx))

for i in range(data.shape[0]):
    canvas[data[i, 1], data[i, 0]] = 1

for i in range(ly):
    print("".join("#" if p else " " for p in canvas[i]))

print(t)

