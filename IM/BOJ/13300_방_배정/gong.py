import sys
sys.stdin = open('input.txt')
N,K = map(int,input().split())
class_lst = [[0,0] for _ in range(7)]
for _ in range(N):
    sex,clas = map(int,input().split())
    class_lst[clas][sex] += 1
cnt = 0
for i in range(1,7):
    for j in range(2):
        if class_lst[i][j] == 0:
            pass
        elif class_lst[i][j]%K == 0:
            cnt += class_lst[i][j]//K
        else:
            cnt += class_lst[i][j]//K + 1
print(cnt)