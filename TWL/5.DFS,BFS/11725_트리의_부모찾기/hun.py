from collections import deque


def bfs(N, arr):
    dq = deque([1])
    mom = [0] * (N + 1)
    while dq:
        now = dq.popleft()
        for num in arr[now]:
            if mom[num] == 0 and num != 1:
                mom[num] = now
                dq.append(num)
    for num in range(2, N+1):
        print(mom[num])


N = int(input())
arr = [[0] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)
bfs(N, arr)
