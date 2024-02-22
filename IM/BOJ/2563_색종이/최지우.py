import sys
sys.stdin = open('input.txt')


arr = [[0] * 100 for _ in range(100)]
N = int(input())

cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if arr[x-1+i][y-1+j] == 1:
                cnt += 1
            else: arr[x-1+i][y-1+j] = 1
result = 100 * N - cnt
print(result)