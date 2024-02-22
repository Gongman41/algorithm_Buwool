import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(int, input().split()))

arr = []
cnt = 1
for i in num:
    left = arr[:i]
    right = arr[i:]
    arr = left + [cnt] + right
    cnt += 1

arr.reverse()
print(*arr)