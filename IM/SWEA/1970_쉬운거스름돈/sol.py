import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*8
    for idx in range(len(arr)):
        result[idx] = N // arr[idx]
        N = N % arr[idx]
    print(f'#{tc}')
    print(*result)