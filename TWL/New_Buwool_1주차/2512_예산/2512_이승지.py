n = int(input())
nums = sorted(list(map(int, input().strip().split())))
m = int(input())

low, high = 0, max(nums)  # 최소, 최대

answer = 0  # 최종 정답 저장
while low <= high:
    total = 0
    mid = (low + high) // 2  # 중간값을 임시 예산으로

    for num in nums:  # 예산에 따라 추가
        total += min(num, mid)

    if total <= m:  # 이 예산으로 계산을 했을 때 한도를 넘지 않는 경우
        low = mid + 1  # 현재 예산 이후로 다음 예측 예산 잡기
        answer = mid  # 일단 현재기준으로 가능한 최고 예산에 대한 결과
    else:  # 한도 초과인 경우
        high = mid - 1  # 현재 예산 이전으로 다음 예측 예산 잡기

print(answer)