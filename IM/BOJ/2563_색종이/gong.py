import sys
sys.stdin = open('input.txt')
matrix = [[0]*100 for _ in range(100)]
cnt = 0
N = int(input())
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            if matrix[i][j] == 0:
                cnt += 1
                matrix[i][j] = 1
print(cnt)
