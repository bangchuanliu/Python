g = {1: [2], 2: [1, 3], 3: [2]}
p = [0] * 4


def dfs(u, p):
    for v in g[u]:
        if v != p[u]:
            p[v] = u
            dfs(v, p)


dfs(1, p)
print(p)
