k, n = map(int, input().split())

cables = []
for _ in range(k):
    cables.append(int(input()))

# 자연수니까
# 손실되는 길이가 될 것 같은 길이는 후보에서 빼줘야하나? 안 빼줘도 되는군..ㅎ
start = 1
end = max(cables)
# 뭐라고 두는 게 좋을까..
max_length = 0

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    for cable in cables:
        cnt += cable//middle
        if cnt >= n:
            break

    if cnt >= n:
        max_length = middle
        start = middle + 1
    else:
        end = middle - 1

print(max_length)