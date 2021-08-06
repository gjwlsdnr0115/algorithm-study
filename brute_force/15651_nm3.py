n, m = map(int, input().split())
res = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, res)))
        return
    for i in range(n):
        res.append(i+1)
        dfs(depth+1, n, m)
        res.pop()

dfs(0, n, m)