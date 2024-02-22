import sys
sys.stdin = open('input.txt')

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))


arr = [[0] * 1002 for _ in range(1002)]
result = {i:0 for i in range(N+1)}
for idx, p in enumerate(paper):
    x, y, w, h = p

    for i in range(x, x+w):
        for j in range(y, y+h):
            result[arr[i][j]] -= 1
            arr[i][j] = idx+1
            result[idx+1] += 1

for i in range(1, N+1):
    print(result[i])