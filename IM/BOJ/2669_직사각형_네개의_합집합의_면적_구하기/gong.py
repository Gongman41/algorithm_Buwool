import sys
sys.stdin = open('input.txt')
matrix_x = 0
matrix_y = 0
sq_lst = []
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    matrix_x = max(matrix_x,x2)
    matrix_y = max(matrix_y,y2)
    sq_lst.append([(x1,x2),(y1,y2)])
matrix = [[0]*101 for _ in range(101)]
cnt = 0
for sq in sq_lst:
    for x in range(sq[0][0],sq[0][1]):
        for y in range(sq[1][0],sq[1][1]):
            if matrix[x][y] == 0:
                matrix[x][y] = 1
                cnt+=1
print(cnt)
        

    
    