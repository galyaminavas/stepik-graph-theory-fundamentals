def bfs(vertex):
    dist[vertex] = 0
    queue = []
    used[vertex] = True
    for sons in g[vertex]:
        queue.append(sons)
        dist[sons] = 1
        used[sons] = True
    while len(queue) != 0:
        curr_v = queue.pop(0)
        #print(curr_v)
        for curr_v_child in g[curr_v]:
            if not used[curr_v_child]:
                queue.append(curr_v_child)
                dist[curr_v_child] = dist[curr_v] + 1
                used[curr_v_child] = True


string1 = input()
v = int(string1.split(' ')[0])
e = int(string1.split(' ')[1])

g = [[] for i in range(v)]
dist = [-1 for j in range(v)]
used = [False for k in range(v)]
#components = 0
for i in range(e):
    a = list(map(int, input().split(' ')))
    g[a[0]].append(a[1])
    g[a[1]].append(a[0])


# for i1 in range(v):
#     print(g[i1])
# print(len(g))
# print(len(dist))
# print(len(used))
# for i in range(v):
#     print(g[v])
bfs(0)

answer = ''
for ans in dist:
    answer += str(ans) + ' '
print(answer)


