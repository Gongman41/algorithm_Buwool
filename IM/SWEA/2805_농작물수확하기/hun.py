import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range(N//2 + 1):
        total += sum(lst[i][N//2 - i:N//2 + i + 1])
    cnt = 1
    # print(total)
    for j in range(N//2+1, N):
        total += sum(lst[j][cnt:N-cnt])
        cnt += 1
    print(f'#{tc} {total}')