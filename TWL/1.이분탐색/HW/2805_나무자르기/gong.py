N,M = map(int,input().split())
M_lst = list(map(int,input().split()))
start, end = 1, max(M_lst)

while start <= end:
    top = 0
    middle = (start+end)//2
    ttree = 0
    for n in range(N):
        if M_lst[n] > middle:
            ttree += M_lst[n]-middle
    
    if M <= ttree:
        start = middle +1
    
    else:
        end = middle -1
print(end)

    

