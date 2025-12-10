# https://adventofcode.com/2025/day/8
# Playground

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day8\day8.input', 'r', encoding='utf-8') as f:
    pts = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

n = len(pts)
edges = []
for i in range(n):
    xi, yi, zi = pts[i]
    for j in range(i + 1, n):
        xj, yj, zj = pts[j]
        dx = xi - xj
        dy = yi - yj
        dz = zi - zj
        edges.append((dx * dx + dy * dy + dz * dz, i, j))

edges.sort(key=lambda e: e[0])

def build_dsu(N):
    par = list(range(N))
    sz = [1] * N
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    def union(x, y):
        xr, yr = find(x), find(y)
        if xr == yr:
            return False
        if sz[xr] < sz[yr]:
            xr, yr = yr, xr
        par[yr] = xr
        sz[xr] += sz[yr]
        return True
    return par, sz, find, union

par, sz, find, union = build_dsu(n)
for k in range(1000):
    _, i, j = edges[k]
    union(i, j)

count = {}
for i in range(n):
    r = find(i)
    count[r] = count.get(r, 0) + 1

sizes = sorted(count.values(), reverse=True)
sol = sizes[0] * sizes[1] * sizes[2] if len(sizes) >= 3 else 0
print(sol)


# Part 2
par, sz, find, union = build_dsu(n)
comp = n
last_i = -1
last_j = -1
for d2, i, j in edges:
    if union(i, j):
        comp -= 1
        last_i = i
        last_j = j
        if comp == 1:
            break

sol = pts[last_i][0] * pts[last_j][0]
print(sol)
