import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간, 시작 시간 순으로 정렬
cnt = 1     # times[0]에 있는 회의는 무조건 가능하니까 1로
now_e = times[0][1]    # 현재 끝나는 회의 시간
for i in range(1, N):
    next_s = times[i][0]    # 다음 회의 시작 시간
    if now_e <= next_s:      # 안 겹치면 회의 가능!
        cnt += 1
        now_e = times[i][1]     # 현재 끝나는 회의 시간 갱신해준다
print(cnt)


