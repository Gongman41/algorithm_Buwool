import sys
sys.stdin = open('input.txt')
N = int(input())
n_list = [list(map(int,input().split())) for _ in range(N)]
sq_lst = []
matrix = [[0]*1001 for _ in range(1001)]
for n in range(N):
    x1,y1,x2,y2 = n_list.pop()
    cnt = 0 
    for i in range(x1,x1+x2):
        for j in range(y1,y1+y2):
            if matrix[i][j] == 0:
                cnt += 1
                matrix[i][j] = 1
    sq_lst.append(cnt)
for _ in range(N):
    print(sq_lst.pop())
