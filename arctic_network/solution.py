import math


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)

    if ra == rb:
        return False

    parent[rb] = ra
    return True


T = int(input())

for _ in range(T):
    S, P = map(int, input().split())

    points = [tuple(map(int, input().split())) for _ in range(P)]

    if S >= P:
        print("0.00")
        continue

    edges = []
    for i in range(P):
        x1, y1 = points[i]
        for j in range(i + 1, P):
            x2, y2 = points[j]
            d = math.hypot(x1 - x2, y1 - y2)
            edges.append((d, i, j))

    edges.sort()

    parent = list(range(P))
    mst = []
    for d, u, v in edges:
        if union(parent, u, v):
            mst.append(d)
            if len(mst) == P - 1:
                break

    print(f"{mst[-S]:.2f}")
