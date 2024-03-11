import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = N
title = []
for _ in range(N):
    t, n = map(str, input().split())
    n = int(n)
    if title and title[-1][1] == n:
        cnt -= 1
    else:
        title.append((t, n))

for _ in range(M):
    tmp = int(input())
    start = 0
    end = cnt-1

    while start <= end:
        mid = (start+end)//2
        if title[mid][1] == tmp:
            start = mid
            break
        elif title[mid][1] > tmp:
            end = mid-1
        else:
            start = mid+1
        
    print(title[start][0])