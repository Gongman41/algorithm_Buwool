from collections import deque

def DFS(start):
    visited_D[start] = 1
    print(start,end=' ')
    if m_lst[start]:
        for i in m_lst[start]:
            if visited_D[i] == 0:
                DFS(i)

def BFS(start):
    deq.append(start)
    visited_B[start] = 1
    while deq:
        st = deq.popleft()

        print(st,end=' ')
        if m_lst[st]:
            for i in m_lst[st]:
                if visited_B[i] == 0:
                    visited_B[i] = 1
                    deq.append(i)



N,M,V = map(int,input().split())
m_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    m_lst[a].append(b)
    m_lst[a].sort()
    m_lst[b].append(a)
    m_lst[b].sort()
visited_D = [0]*(N+1)
visited_B= [0]*(N+1)
DFS(V)
deq = deque([])
print()
BFS(V)
