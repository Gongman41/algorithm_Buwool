import sys
sys.stdin = open('input.txt')


N = int(input())
arr = list(map(int, input().split()))

cnt = 1
line = [0]
for idx, i in enumerate(arr, 1):
    line.insert(cnt - i, idx)
    cnt += 1
print(*line[1:])