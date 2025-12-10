# https://adventofcode.com/2025/day/9
# Movie Theater

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day9\day9.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [l.split(',') for l in lines]
    lines = [[int(x) for x in l] for l in lines]

memo = 0
memo_l = []
memo_m = []
for l in lines:
    for m in lines:
        if (abs(l[0]-m[0])+1)*(abs(l[1]-m[1])+1) > memo:
            memo = (abs(l[0]-m[0])+1)*(abs(l[1]-m[1])+1)
            memo_l = l
            memo_m = m
print(memo)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day9\day9.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [l.split(',') for l in lines]
    lines = [[int(x) for x in l] for l in lines]

horizontales = []
for i in range(len(lines)):
    x1, y1 = lines[i]
    x2, y2 = lines[(i+1) % len(lines)]
    if y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        horizontales.append((y1, a, b))

def intervalos_en_x(x, horizontales):
    ys = []
    for (y, a, b) in horizontales:
        if a <= x < b:
            ys.append(y)

    ys = sorted(set(ys))

    intervalos = []
    for i in range(0, len(ys), 2):
        if i+1 < len(ys):
            intervalos.append((ys[i], ys[i+1]))

    return intervalos


max_area = 0
best_a = None
best_b = None

for p in lines:
    for q in lines:
        x1, y1 = p
        x2, y2 = q

        xa, xb = sorted([x1, x2])
        ya, yb = sorted([y1, y2])

        int1 = intervalos_en_x(xa, horizontales)
        int2 = intervalos_en_x(xb, horizontales)

        ok1 = any(ya >= a and yb <= b for a, b in int1)
        ok2 = any(ya >= a and yb <= b for a, b in int2)

        if ok1 and ok2:
            area = (xb - xa + 1) * (yb - ya + 1)
            if area > max_area:
                max_area = area
                best_a = p
                best_b = q

print(max_area)
