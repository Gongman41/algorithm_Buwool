import sys
input = sys.stdin.readline

N = int(input())
memo = {input().strip():i for i in range(N)}

passed = [memo[input().strip()] for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if passed[i] >= passed[j]:
            cnt += 1; break
print(cnt)