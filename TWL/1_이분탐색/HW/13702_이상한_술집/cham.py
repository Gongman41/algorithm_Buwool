import sys
sys.stdin = open('input.txt')

# n: 주전자의 개수
# k: 사람 수
n, k = map(int, input().split())
ml = [int(input()) for _ in range(n)]
start = 1
end = max(ml)   # 822
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2    # 411
    for mak in ml:
        cnt += mak // mid
    if cnt >= k:    # 일단 사람 수 넘겼으면
        start = mid + 1
        result = mid    # result에 저장해주고
    else:
        end = mid - 1
print(result)




# # 이렇게 하면 cnt가 k보다 커지는 경우 처리 못 함!!
# start = 0
# end = n - 1
# cnt = 0
# result = 0
# mid = ml[end] // 2  # mid: ml에서 젤 큰 값을 2로 나눈 거
# while cnt <= k:
#     if mid <= ml[start]:    # mid가 ml의 젤 작은 값보다 작거나 같다면(= 나눌 수 있다면)
#         result = mid
#         for mak in ml:
#             cnt += mak // mid
#         mid //= 2
#     else:
#         mid //= 2
# print(result)