def dfs(cur_vertex):
    used[cur_vertex] = True
    # print(cur_vertex + 1)
    for i in g[cur_vertex]:
        if not used[i]:
            dfs(i)


string1 = input()
v = int(string1.split(' ')[0])
e = int(string1.split(' ')[1])

g = [[] for i in range(v)]
used = [False for i in range(v)]
components = 0
for i in range(e):
    a = list(map(int, input().split(' ')))
    g[a[0] - 1].append(a[1] - 1)
    g[a[1] - 1].append(a[0] - 1)

for i in range(v):
    if not used[i]:
        dfs(i)
        components = components + 1

print(components)
# print(v)
# print(e)
