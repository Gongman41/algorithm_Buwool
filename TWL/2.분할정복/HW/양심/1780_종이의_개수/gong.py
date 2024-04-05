def cut(x1,x2,y1,y2,n):
    global minus
    global zero
    global one
    num = matrix[x1][y1]
    if n==1:
        if num == 1:
            one +=1
        elif num == 0:
            zero += 1
        else:
            minus += 1
        return
    check = False
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if matrix[i][j] != num:
                for k in range(x1,x2+1,n//3):
                    for m in range(y1,y2+1,n//3):
                        
                        cut(k,k+n//3-1,m,m+n//3-1,n//3)
                check = True
                break
        if check == True:
            break  
    else:
        if num == 1:
            one +=1
        elif num == 0:
            zero += 1
        else:
            minus += 1
             
    
            
        

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
minus = 0
zero = 0
one = 0
cut(0,N-1,0,N-1,N)
print(minus)
print(zero)
print(one)