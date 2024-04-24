# 흠...!!!!!!!!!!!!!

import sys
input = sys.stdin.readline

def is_finish(winner):
    key = winner + winner + winner
    if key in [''.join(row) for row in board]: # 행 검사
        return True
    if key in [''.join([row[i] for row in board]) for i in range(3)]: # 열 검사
        return True
    # 대각선 검사

    return False

def is_valid(x, o):
    # x는 5개, o는 4개가 최대
    if (x > 5) or (o > 4):
        print('invalid')
        return
    valid = False
    of, xf = is_finish('O'), is_finish('X')

    # O가 이겨야함

    # X가 이기거나 / 둘다 못이겼지만 가득차야함

    if valid:
        print('valid')
    else:
        print('invalid')

while True:
    board = input().rstrip()
    if board == 'end':
        break
    x, o = board.count('X'), board.count('O')
    board = [list(board[i:i+3]) for i in range(0, 7, 3)]
    is_valid(x, o)