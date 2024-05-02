import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_diameter(node):
    global result

    tmp_w = []
    f = s = 0
    while tree[node]:
        tmp_w.append(find_diameter(tree[node].pop()))
    tmp_w.sort()
    if len(tmp_w) > 1:
        s, f = tmp_w[-2:]
    elif tmp_w:
        f = tmp_w[0]

    result = max(result, f+s)

    return weight[node] + f


N = int(input())

tree = [[] for _ in range(N+1)]
weight = [0] * (N+1)

for _ in range(N-1):
    p, c, w = map(int, input().split())
    tree[p].append(c)
    weight[c] = w

result = 0
find_diameter(1)
print(result)