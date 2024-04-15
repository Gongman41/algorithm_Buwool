import sys
sys.stdin = open('input.txt')

def dfs(idx, result):
    global max_result, min_result, plus, minus, mul, div
    if idx == n:    # 사칙연산을 다 넣어줬다면
        max_result = max(result, max_result)    # 최대, 최솟값 비교한 후 return
        min_result = min(result, min_result)
        return
    if plus:    # + 연산자가 남아있을 경우
        plus -= 1
        dfs(idx + 1, result + nums[idx])
        plus += 1
    if minus:   # - 연산자가 남아있을 경우
        minus -= 1
        dfs(idx + 1, result - nums[idx])
        minus += 1
    if mul:     # * 연산자가 남아있을 경우
        mul -= 1
        dfs(idx + 1, result * nums[idx])
        mul += 1
    if div:     # / 연산자가 남아있을 경우
        div -= 1
        dfs(idx + 1, int(result / nums[idx]))
        div += 1


n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))
max_result = -1e9
min_result = 1e9
dfs(1, nums[0])     # 연산자 수는 피연산자 수보다 하나 작으니까 걍 1부터 시작
print(max_result)
print(min_result)