import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    n, m = map(int, input().split())
    arr_1 = list(map(int, input().split()))     # n개의 숫자
    arr_2 = list(map(int, input().split()))     # m개의 숫자

    result = 0
    for i in range(abs(n-m) + 1):  # sum 결과
        sum_num = 0
        if n < m:   # nm 중 작은 걸로 돌아야 함
            for j in range(n):  # 0 1 2
                sum_num += arr_1[j] * arr_2[j + i]
        else:
            for j in range(m):  # nm 중 작은 걸로 돌아야 함
                sum_num += arr_1[j + i] * arr_2[j]
        if sum_num > result:
            result = sum_num

    print(f'#{test} {result}')
