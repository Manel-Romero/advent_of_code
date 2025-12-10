# https://adventofcode.com/2025/day/3
# Gift Shop

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day3\day3.input', 'r', encoding='utf-8') as f:
    banks = [x for x in f.read().split()]

sol = 0

for bank in banks:
    maxJoltBattery = 0
    secJoltBattery = 0
    for i in range(len(bank)):
       if int(bank[i]) > maxJoltBattery and i < len(bank)-1:
           maxJoltBattery = int(bank[i])
           lastI = i+1
    bank = bank[lastI:]
    for j in range(len(bank)):
        if int(bank[j]) > secJoltBattery and j < len(bank):
           secJoltBattery = int(bank[j])
    
    sol += (maxJoltBattery*10 + secJoltBattery)

print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day3\day3.input', 'r', encoding='utf-8') as f:
    banks = [x for x in f.read().split()]

sol = 0

for bank in banks:
    for n in range(11,-1,-1):
        maxJoltBattery = 0
        lastI = 0
        for i in range(len(bank)):
            if int(bank[i]) >= maxJoltBattery and i <= len(bank)-n:
                maxJoltBattery = int(bank[i])
                lastI = i
        bank = bank[lastI+1:]
    
        sol += maxJoltBattery*(10**n)

print(sol)
