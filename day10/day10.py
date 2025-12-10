# https://adventofcode.com/2025/day/10
# Factory

from collections import deque
import pulp


# Part 1
with open(r'c:\CP_UPV\advent_of_code\day10\day10.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [l.split(' ') for l in lines]

sol = 0
for l in lines:
    obj = l[0][1:-1]
    n = len(obj)
    target_mask = 0
    for i in range(n):
        if obj[i] == '#':
            target_mask |= 1 << i

    masks = []
    for a in l[1:-1]:
        idxs = [int(x) for x in a.strip('()').split(',') if x != '']
        m = 0
        for b in idxs:
            m |= 1 << b
        masks.append(m)

    dist = [-1] * (1 << n)
    dist[0] = 0
    q = deque([0])
    while q:
        s = q.popleft()
        if s == target_mask:
            sol += dist[s]
            break
        for m in masks:
            ns = s ^ m
            if dist[ns] == -1:
                dist[ns] = dist[s] + 1
                q.append(ns)
print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day10\day10.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [l.split(' ') for l in lines]

sol = 0

for l in lines:
    t = list(map(int, l[-1].strip('{}').split(',')))
    n = len(t)
    m = len(l) - 2

    matrix = []
    for i in range(n):
        row = []
        for btn in l[1:-1]:
            idxs = [int(x) for x in btn.strip('()').split(',') if x != '']
            row.append(1 if i in idxs else 0)
        matrix.append(row)

    prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(m)]
    prob += pulp.lpSum(x)

    for i in range(n):
        prob += pulp.lpSum(matrix[i][j] * x[j] for j in range(m)) == t[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    sol += sum(int(v.varValue) for v in x)

print(sol)
