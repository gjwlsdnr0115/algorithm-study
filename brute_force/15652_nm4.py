n, m = map(int, input().split())
res = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, res)))
        return
    for i in range(idx, n):
        res.append(i+1)
        dfs(depth+1, i, n, m)
        res.pop()

dfs(0, 0, n, m)