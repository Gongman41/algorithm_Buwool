# 선분 0, 선분1, 선분2
import sys
d1 = [0,0,0,1,2,2,3,6]
d2 = [3,4,1,4,4,5,4,7]
d3 = [6,8,2,7,6,8,5,8]
while True:
    tictac = input()
    if tictac == 'end':
        break
        
    x_line = 0
    o_line = 0
    x_cnt = 0
    o_cnt = 0
    for i in range(9):
        if tictac[i] == 'X':
            x_cnt +=1
        elif tictac[i] == 'O':
            o_cnt += 1
        if i != 8:
            if tictac[d1[i]] == tictac[d2[i]] and tictac[d2[i]] == tictac[d3[i]] and tictac[d1[i]] == 'O':
                o_line += 1
            elif tictac[d1[i]] == tictac[d2[i]] and tictac[d2[i]] == tictac[d3[i]] and tictac[d1[i]] == 'X':
                x_line += 1
    if (x_cnt == o_cnt) or (x_cnt == o_cnt +1) :
        if x_line == 2 and o_line == 0 and x_cnt == 5 and o_cnt ==4:
            print('valid')
        elif (x_line == 1 and o_line == 0) and x_cnt == 1+o_cnt:
            
            print('valid')
        elif (x_line == 0 and o_line == 1) and x_cnt == o_cnt:
            print('valid')
        elif x_line == 0 and o_line == 0 and x_cnt == 5 and o_cnt == 4:
            print('valid')
        else:
            print('invalid')
            # no vaild
    else:
        print('invalid')