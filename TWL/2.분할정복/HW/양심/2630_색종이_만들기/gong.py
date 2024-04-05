def check(x1,x2,y1,y2):
    global blue
    global white
    
    color = matrix[x1][y1]
    checkk = False
    if x2==x1:
        if color == 1:
            blue += 1
        else:
            white += 1
        return
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if matrix[i][j] != color:
                check(x1,(x1+x2)//2,y1,(y1+y2)//2)
                check((x1+x2)//2+1, x2, y1, (y1+y2) // 2)
                check((x1+x2)//2+1, x2, (y1+y2)//2+1, y2)
                check(x1, (x1+x2) // 2 , (y1+y2) // 2+1 ,y2)
                checkk = True
                break
        if checkk == True:
            break
    else:
        if color == 1:
            blue += 1
        else:
            white += 1


                


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
blue = 0
white = 0
check(0,N-1,0,N-1)
print(white)
print(blue)
