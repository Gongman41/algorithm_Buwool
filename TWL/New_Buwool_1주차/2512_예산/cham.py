import sys
sys.stdin = open('input.txt')

N = int(input())
budget = list(map(int, input().split()))
budget.sort()
total_budget = int(input())

start, end = 0, budget[-1]
while start <= end:
    result = 0
    mid = (start + end) // 2    # 여기서 중간값 = 상한액
    for b in budget:
        if b <= mid:    # 해당 예산액이 상한액보다 작으면
            result += b     # 걍 그 예산액만큼 결과에 더해준다
        else:       # 해당 예산액이 상한액보다 크면
            result += mid   # 상한액만큼 결과에 더 해줌

    if result <= total_budget:  # 반복문 다 돌고 나서 result 값이 총 예산액보다 작다면
        start = mid + 1     # 상한액을 좀 올려야 ...
    else:
        end = mid - 1

print(end)