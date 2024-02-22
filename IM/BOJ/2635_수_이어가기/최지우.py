import sys
sys.stdin = open('input.txt')

N = int(input())

ans = []
tmp = 0
for i in range(N, 0, -1):
    arr = [N, i]
    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2]-arr[-1])
    
    tmp = max(tmp, len(arr))

    if tmp == len(arr):
        ans = arr
print(len(ans))
print(*ans)