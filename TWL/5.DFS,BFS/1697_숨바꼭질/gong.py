from collections import deque
N,K = map(int,input().split())
deq = deque([])
deq.append([N,0])
visited = [0]*100001
visited[N] = 1
min_time = 10e10
while deq:
    cur,time = deq.popleft()
    if cur == K:
        min_time = min(time,min_time)
        continue
    if time >= min_time:
        continue
    if 0 <= cur + 1 <= 100000 and visited[cur+1]==0:
        deq.append([cur+1,time+1])
        visited[cur+1] = 1
    if 0 <= cur -1 <= 100000 and visited[cur-1]==0:
        deq.append([cur-1,time+1])
        visited[cur-1] = 1
    if 0<= 2*cur <= 100000 and visited[2*cur] == 0:
        deq.append([2*cur,time+1])
        visited[2*cur] = 1
print(min_time)

