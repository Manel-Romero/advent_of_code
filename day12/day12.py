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

sol = 0
for w, h, counts in regions:
    area_total = sum(areas[idx] * c for idx, c in enumerate(counts))
    if area_total <= w * h:
        sol += 1
print(sol)
