# 위상 정렬 알고리즘은 써클이 없는 방향 그래프에서의 !탐색 순서!를 파악할 때
from collections import deque

n,m = map(int,input().split())
table = [[] for _ in range(n+1)]
res = [0]*(n+1) # n번째 과목이 몇 학기에 이수할 수 있는지 저장할 리스트
pre = [0]*(n+1) # 선수과목(진입차수, 진입시 필요한 노드, 부모 노드) 있는지 볼 거임, 뭐가 있는지는 안 봐도 됨 숫자만 cnt

for _ in range(m):
    a,b = map(int, input().split())
    table[a].append(b)
    pre[b] += 1

# 이수한 과목
dq = deque()

# 먼저 초기상태에서 선수과목이 필요 없는 거 뭐 있는지 볼 거임
# 이수 가능 학기와 같이 넣어줌
for i in range(1, n+1):
    if pre[i] == 0:
        dq.append([i,1])
        

while dq:
    node, cnt = dq.popleft()
    # 이수 학기 리스트에 넣어줌, 순서대로 잘 출력하고 싶다잉
    res[node] = cnt

    for i in table[node]:
        pre[i] -= 1
        if pre[i] == 0:
            dq.append([i, cnt+1])

print(*res[1:])