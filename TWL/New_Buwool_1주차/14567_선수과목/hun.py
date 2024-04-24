from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    in_degree[b] += 1

result = [1] * (n+1)
dq = deque([])

for num in range(1, n+1):
    if in_degree[num] == 0:
        dq.append(num)

while dq:
    check_1 = dq.popleft()
    for j in lst[check_1]:
        in_degree[j] -= 1
        if in_degree[j] == 0:
            dq.append(j)
        result[j] = max(result[j], result[check_1] + 1)

result = result[1:]
print(*result)
