import math
X,Y = map(int,input().split())
if X == Y:
    print(-1)

#     # (Y+a)/(X+a) >= Y/X + 0.01
#     # (Y-X)/(X+a) ?= Y/X - 0.99
#     # X + a = (Y-X)/((Y/X)-0.99)
# else:
#     Z = 100*(Y-X)/((Y*100//X)-99) - X
#     if Z != int(Z):
#         print(int(Z)+1)
#     else:
#         print(int(Z))

elif Y*100//X == 99:
    print(-1)
else:
    def ezin(start,end,x,y):
        if start > end:
            print(start)
            return
        
        middle = (start+end)//2
        if y*100//x < (y+middle)*100//(x+middle):
            ezin(start,middle-1,x,y)
        else:
            ezin(middle+1,end,x,y)
            
    ezin(1,X,X,Y)
    
