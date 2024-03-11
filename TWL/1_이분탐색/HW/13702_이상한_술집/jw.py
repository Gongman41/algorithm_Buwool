N, K = map(int, input().split())
ml = [int(input()) for _ in range(N)]

start = 0
end = max(ml)
if end == 0:
    start = 1
elif end == 1:
    if N == K:
        start = 2
    else:
        start = 0
else:
    while start <= end:
        mid = (start+end)//2
        
        tmp = 0
        for i in ml:
            tmp += i//mid
        if tmp >= K:
            start = mid + 1
        elif tmp < K:
            end = mid - 1
        
print(start-1)
