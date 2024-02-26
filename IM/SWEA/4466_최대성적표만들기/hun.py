import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    result = []
    for _ in range(K):
        result.append(lst.pop())
    print(f'#{tc} {sum(result)}')