N = int(input())
Node = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
queue = [1]
while queue:
    cur = queue.pop()
    if graph[cur]:
        for i in graph[cur]:
            if Node[i] == 0:
                Node[i] = cur
                queue.append(i)
for i in range(2,N+1):
    print(Node[i])
    

