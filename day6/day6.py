# https://adventofcode.com/2025/day/6
# Trash Compactor

with open(r'c:\CP_UPV\advent_of_code\day6\day6.input', 'r', encoding='utf-8') as f:
    rows = [r.split() for r in f.read().splitlines()]

a, b, c, d = (list(map(int, rows[i])) for i in range(4))
ops = rows[4]

sol = 0
for op, x1, x2, x3, x4 in zip(ops, a, b, c, d):
    if op == '+':
        sol += x1 + x2 + x3 + x4
    elif op == '*':
        p = x1
        p *= x2
        p *= x3
        p *= x4
        sol += p

print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day6\day6.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

width = max(len(l) for l in lines)
grid = [l.ljust(width) for l in lines]

a, b, c, d = grid[:4]
ops = grid[4]

sol = 0
current_numbers = []
current_op = None

for col in range(width - 1, -1, -1):
    is_separator = (a[col] == ' ' and b[col] == ' ' and c[col] == ' ' and d[col] == ' ')

    if is_separator:
        if current_numbers:
            if current_op == '+':
                sol += sum(current_numbers)
            elif current_op == '*':
                prod = 1
                for n in current_numbers:
                    prod *= n
                sol += prod
        current_numbers = []
        current_op = None
        continue

    num_str = ''.join(ch for ch in (a[col], b[col], c[col], d[col]) if ch.isdigit())
    if num_str:
        current_numbers.append(int(num_str))

    op_ch = ops[col]
    if op_ch in ('+', '*'):
        current_op = op_ch

if current_numbers:
    if current_op == '+':
        sol += sum(current_numbers)
    elif current_op == '*':
        prod = 1
        for n in current_numbers:
            prod *= n
        sol += prod

print(sol)
