# https://adventofcode.com/2025/day/11
# Reactor

import networkx as nx
# Part 1
with open(r'c:\CP_UPV\advent_of_code\day11\day11.input', 'r', encoding='utf-8') as f:
    graph = {}
    for line in f:
        node, neighbors = line.split(':', 1)
        node = node.strip()
        graph[node] = neighbors.strip().split()

circuit = nx.DiGraph()
for u, nbrs in graph.items():
    for v in nbrs:
        circuit.add_edge(u, v)

order = list(nx.topological_sort(circuit))
dp = {n: 0 for n in order}
dp['you'] = 1
for n in order:
    for v in circuit.successors(n):
        dp[v] += dp[n]

print(dp['out'])


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day11\day11.input', 'r', encoding='utf-8') as f:
    graph = {}
    for line in f:
        node, neighbors = line.split(':', 1)
        node = node.strip()
        graph[node] = neighbors.strip().split()

circuit = nx.DiGraph()
for u, nbrs in graph.items():
    for v in nbrs:
        circuit.add_edge(u, v)

nodes = ['svr', 'fft', 'dac', 'out']
order = list(nx.topological_sort(circuit))
sol = 1

for m in range(len(nodes)):
    dp = {n: 0 for n in order}
    dp[nodes[m]] = 1
    for n in order:
        for v in circuit.successors(n):
            dp[v] += dp[n]
    if m+1 < len(nodes):
        sol *= dp[nodes[m+1]]

print(sol)
