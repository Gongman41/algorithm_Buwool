import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_par(x):
    if par[x] != x:
        par[x] = find_par(par[x])
    return par[x]


def union(x, y):
    x = find_par(x)
    y = find_par(y)
    if x < y:
        par[y] = x
    else:
        par[x] = y


n, m = map(int, input().split())

par = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd:
        if find_par(a) == find_par(b):
            print('YES')
            continue
        print('NO')
    else:
        union(a, b)