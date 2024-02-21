import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 11):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N < M:   # M이 더 길다면
        Ai, Bj = Bj, Ai # 두 값을 바꿔서 항상 변수 N에 든 값이 더 길도록 바꾼다.
        N, M = M, N

    result = 0  # 최대 값
    for i in range(N-M + 1):  # 두 배열의 길이의 차 만큼 진행
        sum = 0  # 각 행별로 계산할 임시 정수
        for j in range(len(Bj)):  # 최소 배열의 길이 만큼만 조사
            sum += Bj[j] * Ai[j + i]
        if sum > result:
            result = sum

    print(f'#{tc} {result}')
