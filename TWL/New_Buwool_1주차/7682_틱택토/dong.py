import sys
sys.stdin = open('input.txt')

'''
게임이 끝날 수 있는 경우의 수
0. 먼저 빙고를 세야함 (이기는 즉시 끝나야하니까):
    0-1. X의 win과, O의 win이 둘다 있을 순 없음.
    0-2. 둘다 있다면 invalid
    1. 일단 게임판이 가득가득 찼을 때
        1-1. 9칸이니까 무조건 X가 5개 O가 4개여야함.
        1-2. 가득 찼는데 다른 경우면 그냥 invalid
    2. 게임판이 가득가득 안찼음
        2-1. 그럼 누군가 게임을 이겨서 끝났다는 것인데
            + 그러려면 최소 3번은 둬야하니까 X가.. 그럼 .이 4칸보단 적거나 같아야함 아니면 invalid
            2-1-1. X가 이겼대 (0에서 체크)
                X가 O보다 1개 많아야함 (왜? X가 항상 먼저두는데, X가 이기는 순간 끝나면, X가 O보다 개수가 항상 많음)
                2-2-1. X가 이기는 경우(세로, 가로, 대각선을 확인해보고) 하나라도 맞음
                    2-3-1. 그럼 O의 경우를 세서 => O는 빙고가 아니여야함
                2-2-2. O가 이기는 경우(세로, 가로, 대각선을 확인해보고) 하나라도 맞음
                    2-3-2. 그럼 X의 경우를 세서 => X는 빙고가 아니여야함.
그럼 빙고를 찾는 로직은 어케 짬?
세로 : 0~2 까지만 보고, 각각의 인덱스에 +3 한값이 다 똑같으면 빙고임 (0,3,6) (1,4,7) (2,5,8) 이렇게
가로 : 0,3,6만 보고, 각각의 인덱스에 +1, +2 한값이 다 똑같으면 빙고임 ()
대각선 : (0,4,8) (2,4,6) 만 확인해보면 된다.
'''

while True:
    game = list(input())
    if game[0] == 'e':
        break
    ## 승리 수를 담아준다.
    winLst = [  ## 세로
              (game[0],game[3],game[6]),
              (game[1],game[4],game[7]),
              (game[2],game[5],game[8]),
                ## 가로
                (game[0],game[1],game[2]),
                (game[3],game[4],game[5]),
                (game[6],game[7],game[8]),
                ## 대각선
                (game[0],game[4],game[8]),
                (game[2],game[4],game[6])
              ] 
    Owin = 0
    Xwin = 0
    ## 승리 리스트 만들기
    for win in winLst: # 승리리스트를 돌아서
        if len(set(win)) == 1 and list(set(win))[0] == 'O':
            # o로 빙고가 완성됨
            Owin += 1 # o가이김
        elif len(set(win)) == 1 and list(set(win))[0] == 'X': 
            # x로 빙고가 완성됨
            Xwin += 1 # x가 이김

    if not game.count('.'):# 게임판이 가득찼을때
        ## 그러려면 X는 5개 O는 4개 그리고 한명이 이기거나 비겨야함. => 마지막은 이긴다고 해도 X가 이겨야함 O가 이긴 상태면, 다 차기 전에 invalid
        if game.count('X') == 5 and game.count('O') == 4 and not Owin:
            print('valid')
        else:
            print('invalid')
    else: ## 게임판이 가득가득 안찼을때
        if [Owin, Xwin].count(0) == 1 and game.count('.') <= 4: # 누군가 한명은 이겼어야 한다.
            if Xwin: # X가 이김
                if game.count('X') - game.count('O') == 1: # X가 O 보다 1개 더 많다면
                    print('valid')
                else:
                    print('invalid')
            elif Owin:
                if game.count('O') - game.count('X') == 0: # O가 X와 개수가 같아야함.
                    print('valid')
                else:
                    print('invalid')
        else:
            print('invalid')
        

        
        


    