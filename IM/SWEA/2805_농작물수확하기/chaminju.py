import sys
sys.stdin = open('input.txt')

# bfs로 풀 수 있다네

T = int(input())
for test in range(1, T+1):
    N = int(input())    # N: 농장의 크기
    value = [list(map(int, input())) for _ in range(N)]
    profit = 0
    for i in range(N):  # 0 1 2 3 4
        n = N // 2      # 중간 인덱스 값 -> 2
        if i <= n:
            sum_lst = value[i][n-i:n+i+1]
        else:   # 중간 인덱스를 넘어갈 경우
            j = N-i-1
            sum_lst = value[i][n-j:n+j+1]
        for k in range(len(sum_lst)):
            profit += sum_lst[k]
    print(f'#{test} {profit}')