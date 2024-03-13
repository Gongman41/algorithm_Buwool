n, k = map(int, input().split())

volume = []
for _ in range(n):
    volume.append(int(input()))

# 자연수니까
# 손실되는 길이가 될 것 같은 길이는 후보에서 빼줘야하나? 안 빼줘도 되는군..ㅎ
start = 1
end = max(volume)
# 뭐라고 두는 게 좋을까..
max_mak = 0

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    for v in volume:
        cnt += v // middle
        if cnt >= k:
            break

    if cnt >= k:
        max_mak = middle
        start = middle + 1
    else:
        end = middle - 1

print(max_mak)