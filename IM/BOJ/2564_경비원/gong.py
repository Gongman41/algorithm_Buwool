import sys
sys.stdin = open('input.txt')
W,H = map(int,input().split())
N = int(input())
shop_pnt = []
result = 0
for _ in range(N+1):
    a,b = map(int,input().split())
    if a == 1:
        shop_pnt.append([b,H])
    elif a== 2:
        shop_pnt.append([b,0])
    elif a == 3:
        shop_pnt.append([0,H-b])
    else:
        shop_pnt.append([W,H-b])
cur = shop_pnt.pop()
for shop in shop_pnt:
    if (cur[1] == H and shop[1] == 0) or (cur[1] == 0 and shop[1] == H):
        result += min(cur[0]+H+shop[0],W-cur[0]+H+W-shop[0])
    elif (cur[0] == W and shop[0] == 0) or (cur[0] == 0 and shop[0] == W):
        result += min(cur[1]+W+shop[1],H-cur[1]+W+H-shop[1])
    else:
        result += abs(cur[0]-shop[0])+abs(cur[1]-shop[1])
print(result)

    

