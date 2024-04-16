import sys
sys.stdin = open('input.txt')

def dfs(now, goal, jump, cnt):
    global result
    if now == goal:
        result = min(cnt, result)
        return
    if now > goal or jump <= 0 or now in fails:
        return
    if (now, jump) in dp:
        if dp[(now,jump)] <= cnt:
            return
    dp[(now, jump)] = cnt
    dfs(now + jump, goal, jump + 1, cnt+1)
    dfs(now + jump, goal, jump, cnt+1)
    dfs(now + jump, goal, jump - 1, cnt+1)

N, M = map(int, input().split())
fails = [int(input()) for _ in range(M)]
dp = {}
result = 1e9
dfs(1, N, 1, 0)
if result == 1e9:
    print(-1)
else:
    print(result)