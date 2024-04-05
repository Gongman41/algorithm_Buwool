import sys

N,M = map(int,sys.stdin.readline().split())
#같으면  pass,배열로

n_list = [['a',-1]]
for _ in range(N):
    a,b = sys.stdin.readline().split()
    b = int(b)
    if n_list[-1][1] != b:
        n_list.append([a,b])
last_start = 1
for _ in range(M):
    t = int(sys.stdin.readline())
    start = last_start
    end = len(n_list)-1
    while start <= end:
        middle = (start+end)//2
        if n_list[middle][1] > t:
            end = middle-1
        elif n_list[middle][1] == t:
            print(n_list[middle][0])
            # last_start = middle
            break
        else:
            start = middle +1
        
    else:
        print(n_list[start][0])
        # last_start = start
    


