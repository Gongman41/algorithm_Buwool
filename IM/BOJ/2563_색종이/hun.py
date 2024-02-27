import sys
sys.stdin = open('input.txt')

visited =[[0]*100 for _ in range(100)]
T = int(input())
cnt = 0
for _ in range(T):
    a, b = map(int, input().split())
    for c in range(a, a+10):
        for d in range(b, b+10):
            if visited[c][d] == 0:
                cnt += 1
                visited[c][d] = 1
print(cnt)