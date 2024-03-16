T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    B = list(map(int,input().split()))
    B.sort()
    cnt = 0
    for n in range(N):
        for m in range(M):
            if A[n] > B[m]:
                cnt += 1
            else:
                break
    print(cnt)

# 크기가 달라지는 첫번째꺼

