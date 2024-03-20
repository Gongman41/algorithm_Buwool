import sys

N = int(sys.stdin.readline())
n_list = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

for m in m_list:
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        
        if m == n_list[middle]:
            print(1,end=' ')
            break
        elif m > n_list[middle]:
            start = middle +1
        else:
            end = middle-1
    else:
        print(0,end=' ')

