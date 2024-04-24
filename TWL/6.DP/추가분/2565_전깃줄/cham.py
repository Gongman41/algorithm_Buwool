import sys
sys.stdin = open('input.txt')

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: x[0])
dp = [1] * n
for i in range(n):
    cnt = 0
    for j in range(i):
        if lines[i][1] > lines[j][1]:   # 증가한다면
            cnt += 1
    dp[i] = cnt

print(n-max(dp))
# 다시 풀어봐라~~~이 쌰갈
