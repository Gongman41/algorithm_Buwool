import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    result = [i for i in range(1, N+1)]
    line = map(int, input().split())
    for i in line:
        result.remove(i)
    print(f'#{tc}', end=' ')
    print(*result)
