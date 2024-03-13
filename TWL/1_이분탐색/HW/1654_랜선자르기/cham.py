import sys
sys.stdin = open('input.txt')

# N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
# k: 지금 가지고 있는 랜선의 개수
# n: 필요한 랜선의 개수
k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
start = 1
end = max(length)
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in length:
        cnt += i // mid
    if cnt >= n:    # 일단 필요한 랜선 갯수 넘겼으면
        start = mid + 1
        result = mid    # result에 저장해주고
    else:
        end = mid - 1

print(result)

