def back_tracking(start, visited_city_cnt, expense):
    global min_expense
    # 만약 도시의 수 - 1개를 돌았으면 이제 볼 게 마지막 도시!
    if visited_city_cnt == n-1:
        # 마지막 도시에서 처음으로 갈 수 있는지 봄
        if city[start][init] > 0:
            # 처음으로 갈 수 있다면 돌아가는 비용을 합산한 비용이 현재 최소 비용보다 작은지 판단하고 더 작은 걸로 업뎃
            if expense + city[start][init] < min_expense:
                min_expense = expense + city[start][init]
        return
    # 여행 루트를 짜는 중간에 비용이 현재까지 본 비용보다 크면 걍 그 루트는 중단
    if expense > min_expense:
        return

    for next in range(n):
        # 0이 아니여야 갈 수 있는 경우이며, 다음 갈 도시가 방문하지 않아야 하며, 초기 시작점을 여행 중간에 돌아가서는 안 되니까!
        if city[start][next] != 0 and visited[next] == 0 and next != init:
            visited[next] = 1
            back_tracking(next, visited_city_cnt + 1, expense + city[start][next])
            visited[next] = 0

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
min_expense = float('inf')
visited = [0 for _ in range(n)]
# i -> j와 j -> i의 비용이 다를 수 있으니까 일단 다 돌아
for i in range(n):
    # 처음 시작점을 구분하기 위해서 일단 변수 줌
    init = i
    back_tracking(i, 0, 0)
print(min_expense)