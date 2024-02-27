import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    # N: 시험 친 과목, K: 선택할 수 있는 과목 수
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    result = 0
    for i in range(K):
        result += score[i]
    print(f'#{test} {result}')