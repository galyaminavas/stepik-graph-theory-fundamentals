def main():
    string1 = input()
    v = int(string1.split(' ')[0])
    e = int(string1.split(' ')[1])

    g = [[] for i in range(v)]
    # used = [False for i in range(v)]
    components = 0
    for i in range(e):
        a = list(map(int, input().split(' ')))
        g[a[0] - 1].append(a[1] - 1)
        g[a[1] - 1].append(a[0] - 1)

    # print(g)

    deg = [0 for i in range(v)]
    for i in range(v):
        deg[i] = deg[i] + len(g[i])

    # print(deg)

    bad = False
    # print(bad)
    for i in range(v):
        if deg[i] == 0 or deg[i] % 2 == 1:
            bad = True
            break
    if bad:
        print("NONE")
        return

    stack = list()
    stack.append(0)
    result = list()
    while len(stack) != 0:
        curr_v = stack.pop()
        if (deg[curr_v]) == 0:
            result.append(curr_v)
        else:
            # print(curr_v, g[curr_v])
            dest = g[curr_v].pop()
            deg[curr_v] = deg[curr_v] - 1
            deg[dest] = deg[dest] - 1
            g[dest].remove(curr_v)
            stack.append(curr_v)
            stack.append(dest)

    for i in range(v):
        if len(g[i]) != 0:
            bad = True

    if bad:
        print("NONE")
    else:
        result.pop()
        for a in result:
            print(a + 1, end=" ")


main()
