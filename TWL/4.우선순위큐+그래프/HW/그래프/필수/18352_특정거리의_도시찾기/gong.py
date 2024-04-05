from collections import deque
# import sys

# sys.stdin = open('input.txt')
N,M,K,X = map(int,input().split())
n_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    n_lst[a].append(b)
deq = deque([[X,0]])
visited = [0]*(N+1)
visited[X] = 1
result = []
while deq:
    cur,cnt = deq.popleft()
    print(cur,cnt)
    if cnt == K:
        result.append(cur)
    if n_lst[cur]:
        for i in n_lst[cur]:
            if visited[i] == 0:
                visited[i] = 1
                deq.append([i,cnt+1])
if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
        
