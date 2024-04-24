import sys
input = sys.stdin.readline

N, M = map(int, input().split())
link = {i:[] for i in range(N+1)}
rev_link = [0 for i in range(N+1)]

start = []
for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    rev_link[b] += 1

for i in range(1, N+1):
    if not rev_link[i]:
        start.append(i)

line = []
while start:
    v = start.pop()
    line.append(v)
    for i in link[v]:
        rev_link[i] -= 1
        if not rev_link[i]:
            start.append(i)

print(*line)
