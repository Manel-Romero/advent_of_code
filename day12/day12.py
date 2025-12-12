# https://adventofcode.com/2025/day/12
# Christmas Tree Farm

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day12\day12.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

regions = []
for l in lines:
    s = l.strip()
    w, h = map(int, s[:5].split("x"))
    counts = list(map(int, s[6:].split()))
    regions.append((w, h, counts))

shapes = [['##.', '.##', '..#'], 
    ['#.#', '###', '#.#'], 
    ['#.#', '###', '.##'],
    ['#.#', '#.#', '###'],
    ['###', '.##', '..#'],
    ['..#', '###', '###']]

areas = [sum(row.count('#') for row in shp) for shp in shapes]
sizes_by_idx = []
for shp in shapes:
    grids = set()
    work = shp
    for _ in range(4):
        new_g = []
        for col in range(len(work[0])):
            s = []
            for row in range(len(work) - 1, -1, -1):
                s.append(work[row][col])
            new_g.append(''.join(s))
        work = new_g
        grids.add(tuple(work))
        flip_g = [row[::-1] for row in work]
        grids.add(tuple(flip_g))
    sizes = []
    for g in grids:
        h2 = len(g)
        w2 = len(g[0])
        xs = []
        ys = []
        for y in range(h2):
            row = g[y]
            for x in range(w2):
                if row[x] == '#':
                    xs.append(x)
                    ys.append(y)
        if xs:
            bw = max(xs) - min(xs) + 1
            bh = max(ys) - min(ys) + 1
            sizes.append((bw, bh))
    sizes_by_idx.append(sorted(set(sizes)))

sol = 0
for w, h, counts in regions:
    area_total = 0
    ok = True
    for idx, c in enumerate(counts):
        if c == 0:
            continue
        area_total += areas[idx] * c
        if not any((bw <= w and bh <= h) or (bw <= h and bh <= w) for bw, bh in sizes_by_idx[idx]):
            ok = False
            break
    if ok and area_total <= w * h:
        sol += 1
print(sol)