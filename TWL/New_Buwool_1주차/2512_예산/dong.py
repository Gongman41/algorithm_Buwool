import sys
sys.stdin = open('input.txt')

'''
예산을 나누어 주어야 하는데, 정해진 총액 이하에서 가능한 최대 예산 배정
모두 줄 수 있으면, 다 준다
모두 줄 수 없으면, 특정 상한액을 찾아서, 그 이상인 예산 요청에 모두 상한을 배정
상한액 이하 요청에 대해선 금액 그대로 배정
'''

N = int(input()) # 지방의 수
budgets = list(map(int,input().split())) # 각 지방의 예산 요청
total   = int(input()) # 보유 예산
if sum(budgets) <= total: # 다 줄 수있으면
    print(max(budgets)) # 그냥 다 주고 최대값 출력
else: # 다 줄 수 없다면
    ## 최선의 값을 탐색해야함 => 이분탐색을 해보자
    result = 0 # 최선 예산을 담을 값
    start = 0 # 시작값
    end = total # 최대값
    while start <= end: # 이분탐색 조건
        now = 0 # 현재 지점에서 담기는 예산
        mid = (start + end) // 2
        for budget in budgets:
            if budget <= mid: # 상한액 이하면
                now += budget # 그걸 주고
            else: # 그걸 넘으면
                now += mid # 상한액을 준다
        if now <= total: # 만약 전체 예산이 배정 가능한 범위인데
            if result < mid: # 그게 최선의 예산 배정이라면
                result = mid # 갱신해주고
                start = mid + 1 # 더 줘본다
        else: # 예산이 배정 가능한 범위가 아님
            end = mid - 1 # 그럼 덜 줘본다.
    print(result)
        