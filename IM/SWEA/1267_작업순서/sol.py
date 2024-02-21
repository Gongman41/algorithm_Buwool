import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(q):
    while q:    # 조사 대상 남아 있는동안
        now = q.popleft()       # 현재위치로부터
        for next in adj[now]:   # 진입 가능 대상 탐색
            '''
                1 -> 2, 3 -> 2 였다면 2번 노드의 진입차수는 2
                1번과 3번이 모두 작업이 완료되어야 2번 작업 가능
                1 -> 2로 이동한다면,
                2번 노드 작업 시작전 필요작업인 1이 완료되었으므로
                2번 노드의 진입차수 1감소
            '''
            orders[next] -= 1           # 해당 노드의 진입차수 1회 차감
            if orders[next] == 0:       # 다음 조사 대상 진입차수가 0이 되었다면
                print(next, end=' ')    # 해당 노드 정보 출력후,
                q.append(next)          # 다음 조사 대상에 추가

for tc in range(1, 11):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    adj = [[] for _ in range(V+1)]   # 인접 리스트
    orders = [0] * (V+1)   # 진입차수

    for i in range(0, E*2, 2):
        adj[edge[i]].append(edge[i+1])  # 유방향 그래프이므로 한 방향만 기록
        orders[edge[i+1]] += 1          # x -> y로 진입하는 횟수를 y번째 orders에 기록

    q = deque()
    print(f'#{tc}', end=' ')
    for i in range(1, V+1): # 0번 노드 없음
        if orders[i] == 0:  # 진입차수가 0인 노드들을
            print(i, end=' ')   # 순서대로 출력하고
            q.append(i)     # 조사 대상에 삽입
    BFS(q)  # 너비우선탐색 진행
    print()