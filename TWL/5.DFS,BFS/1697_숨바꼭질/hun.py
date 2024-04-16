from collections import deque

start, end = map(int, input().split())

# 5, 17
# 10, 9, 18, 17 --> 4초
# bfs 로 조져 봅시다 가장 짧게 가야하니까
# 값을 저장해두고 중간에 4초 나오면 출력 탈출
# 렛츠고
result_lst = [0]*(100001)
result_lst[start] = 1
def bfs(start):
    dq = deque([start])
    # print(dq)
    while dq:
        # print(dq)
        cx = dq.popleft()
        if cx == end:
            print(result_lst[cx]-1)
            break
        for nx in [2*cx, cx+1, cx-1]:
            if 0 <= nx <= 100000 and result_lst[nx] == 0:
                result_lst[nx] = result_lst[cx] + 1
                dq.append(nx)
bfs(start)