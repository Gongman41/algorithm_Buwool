import sys
sys.stdin = open('input.txt')

'''
1부터 N번호 까지의 도시들이 있고, 도시들 사이엔 길(없을 수도 있음)
이제 한 외판원이 어느 도시에서 출발해 도시를 모두 거쳐, 다시 시작점으로 돌아오는 여행
단 한번 갔던 도시로는 다시 갈 수 없고(한붓그리기?), 가장 적은 비용의 여행
각 도시간의 비용은 2차원 배열, W[i][j] => i 에서 j 로 가는 비용 (서로 비용은 다를 수 있음)
0이면 못가는거임
그럼 백트래킹으로 문제를 해결할 수 있을까
재귀로 넣어서, 4라고 쳤을때, 0에서 1,2,3 중 갈 수 있는 도시넣어보고 방문처리

'''
def trip(now, sumi, cnt, start):
    global mini
    if cnt == n-1:  # 전부 여행을 다했으면
        if cities[now][start]: # 해당 지점에서 출발점으로 돌아갈 수 있다면
            mini = min(mini, sumi + cities[now][start]) # 최소비용으로 갱신    
            return
    if sumi > mini: # 이미 여행 비용을 넘으면
        return
    else:
        for i in range(n):
            if not visited[i] and cities[now][i]:#방문을 안했고 갈 수 있으면
                visited[i] = 1 # 방문표시
                trip(i, sumi+cities[now][i], cnt + 1, start) # 재귀를 돌려주고
                visited[i] = 0 # 재귀가 끝났으면 방문표시 빼준다
            
n = int(input())
cities = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
mini = 1e9
for i in range(n): # 시작지점을 다 바꿔본다.
    visited[i] = 1 # 시작점의 방문체크
    trip(i, 0, 0, i)
    visited[i] = 0 # 원상복귀
print(mini)
    

