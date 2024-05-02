
'''
사이클이 없는 무방향 그래프
둘 사이 항상 하나의 간선
가장 길게 늘어나는 경우 => 가장 긴 간선의 차이
해당 두 노드 사이의 거리를 지름으로 본다.
각 간선의 가중치가 존재했을때, 지름을 고르면 된다.
그냥 두 노드 사이의 가중치가 가장 큰 것을 고르면 되는데
완탐 => 시간초과 ...
그럼 가장 긴 거리란.. 어차피 가중치가 - 가 아닌이상
가장 최고의 부모 1 부터 젤 먼걸 구하고,
그 먼거에서 가장 먼걸 구하면 그게 지름이다
이걸 어케 구현함?
먼저, dfs 로 접근했다고 생각했을때,
1을 now값으로 넣어주고(가장 최상단의 부모(문제에 트리는 1부터 n까지라 되어있음))
어차피 트리에 넣어주고, 다음값들을 지속적으로 탐색하는 것과 같다.
그럼 이전값과 현재값만 넣어주고, 그 트리에서 이전값이 지금 가려고하는 값이랑 같지만 않다면 가볼수 있음 (젤 멀리 가야하니까)
그럼 해당 값에서 가장 큰 값을 리턴해주고,
만약 끝까지 가서 그 비용이 젤 크면
지금 까지 온 것과 남은 비용을 더해주고
만약 두번째 보다 크다면
그건 최장 노드로 가기 이전에 1로부터 가장 큰 노드를 찾은 값이니까
이를 새로 갱신해준다. 그러니까 사실상 1로 부터 가장 큰 노드로 간다는 것은
가장 큰 노드로 부터 가장 큰 노드로 가는 이전 단계이기보다
가장 큰 노드에서 가장 큰 노드를 찾기 위한 중첩과정으로 볼 수 있다?
'''

import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)
def dfs(now, back):
    global maxi
    first = 0
    second = 0

    for next, weight in tree[now]:
        if next != back:
            cost = dfs(next, now) + weight
            if cost > first:
                second = first
                first = cost
            elif cost > second:
                second = cost
        
    maxi = max(maxi, first + second)
    return first

n = int(input()) # 노드의 개수
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    # 방향이 없는 그래프 생성
    parent, child, weight = map(int,input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

maxi = 0
dfs(1, 0)
print(maxi)
