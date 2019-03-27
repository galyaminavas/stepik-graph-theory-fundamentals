import sys
from collections import defaultdict


adj = defaultdict(list)
used = []
tin = []
fup = []
timer = 0
cutpoints = set()


def dfs(v, p):
    used[v] = True
    global timer
    timer += 1
    tin[v] = fup[v] = timer
    children = 0
    for to in adj[v]:
        if to == p:
            continue
        if used[to]:
            fup[v] = min(fup[v], tin[to])
        else:
            dfs(to, v)
            fup[v] = min(fup[v], fup[to])
            if fup[to] >= tin[v] and p != -1:
                cutpoints.add(v)
            children = children + 1

    if p == -1 and children > 1:
        cutpoints.add(v)


sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)
edges = list(tuple(map(int, line.split())) for line in sys.stdin)

for i in range(len(edges)):
    adj[edges[i][0]].append(edges[i][1])
    adj[edges[i][1]].append(edges[i][0])

for i in range(len(adj)):
    used.append(False)
    fup.append(0)
    tin.append(0)

dfs(0, -1)
for cp in cutpoints:
    print(cp, end=' ')
