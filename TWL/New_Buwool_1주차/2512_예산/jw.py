N = int(input())
bud = list(map(int, input().split()))
total = int(input())

bud.sort(reverse=True)
k = sum(bud)
if k < total:
    print(bud[0])
else:
    start = 0
    end = bud[0]

    while start <= end:
        mid = (start+end)//2
        tmp = 0

        for i in range(N):
            if bud[i] <= mid:
                tmp += bud[i]
            else:
                tmp += mid

        if tmp < total:
            start = mid + 1
        elif tmp > total:
            end = mid - 1
        else:
            start = mid
            break

    else:
        start -= 1

    print(start)