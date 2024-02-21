import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 매번 1칸씩 증가하면서 값을 더해간다
# 즉, 이번 조사 시작 범위의 바로 앞칸의 값을 제거하고, 이번 조사 범위의 값을 더하면
# 내가 원하는 이번 조사 범위의 값이 된다.
memo = [0] * (N - K + 1)
tmp = 0
# 첫 번째 범위 계산
for i in range(K):
    tmp += arr[i]
memo[0] = tmp
# 최댓값 연산용 값 초기화
result = tmp

'''
범위 3인경우
2 1 3 -3 2 5
첫 범위 : 0 ~ 2 | 2 + 1 + 3
[6, 0, 0, 0]    -> 각 범위의 합들을 기록할 곳

다음 범위 : 1 ~ 3 | 1 + 3 + -3
이때, (1 + 3) 의 값은 첫번째 범위의 합 6에서 0번쨰 값 2를 뺀것과 같음
즉, 2번째 조사 범위는 아래와 같다. 
0-2번 범위 계산  - 0번째 값 + 3번째 값
0 | 1 | 2 | 3
2 | 1 | 3 |-3
(2 + 1 + 3) - 2 + (-3) 
[6, 1, 0, 0]
이하 동일.
[6, 1, 2, 4]    => 그 중 최댓값
'''
for i in range(K, N):
    tmp = memo[i-K] - arr[i-K] + arr[i]
    memo[i-K+1] = tmp
    if result < tmp:
        result = tmp
print(result)