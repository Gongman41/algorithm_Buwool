from collections import deque

def indoor(now):
    now_cnt = 0
    visited[now] = 1
    for next in adj_list[now]:
        if visited[next] == 0 and place[next] == 1:
            # next도 visited하면 그거랑 연결된 걸 볼 수가 없다
            # 어차피 next가 0이면 그 왕복 경로는 구한 걸로 알고 pass함
            now_cnt += 2
    return now_cnt

def outdoor(start):
    indoor_cnt = 0
    dq = deque([start])
    visited[start] = 1

    while dq:
        now = dq.popleft()

        for next in adj_list[now]:
            if place[next] == 1:
                indoor_cnt += 1
            else:
                if visited[next] == 0:
                    visited[next] = 1
                    dq.append(next)

    return indoor_cnt * (indoor_cnt-1)

n = int(input())
# 1이 실내(시작과 끝), 0이 실외
place = list(map(int, input()))
place.insert(0, 0)

adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    node1, node2 = sorted(map(int, input().split()))
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

cnt = 0
visited = [0] * (n+1)
for start in range(1, n+1):
    # 실내면 실내 - 실내만 찾음
    if place[start] == 1:
        cnt += indoor(start)
    # 실외면 조합으로 경로 구함, 이미 본 조합은 안 봐야하니까
    else:
        if visited[start] == 0:
            cnt += outdoor(start)

print(cnt)