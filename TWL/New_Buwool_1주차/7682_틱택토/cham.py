import sys
sys.stdin = open('input.txt')

# X가 선공
# 다 찼다면 X가 하나 더 많아야 함
# o가 이겼으면 x 개수 = o 개수
# x가 이겼으면 x 개수가 하나 더 많음

win_idx = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def win_x(x_data):
    for win in win_idx:
        if win in X_idx:
            return True
        else:
            continue
    else:
        return False


def win_o(o_data):
    for win in win_idx:
        if win in O_idx:
            return True
        else:
            continue
    else:
        return False


while True:
    board = input()
    if board == 'end':
        break
    O_num, X_num = 0, 0
    O_idx, X_idx = [], []
    for i in range(len(board)):
        if board[i] == 'O':
            O_num += 1
            O_idx.append(i)
        elif board[i] == 'X':
            X_num += 1
            X_idx.append(i)
    # print(O_idx, X_idx)
    # print(O_num, X_num)
    if O_num < 3 and X_num < 3:
        print('invalid')
    elif X_num == (O_num + 1):    # X가 이길 수 있음
        if win_x(X_idx):    # 예상대로 x가 이기면
            print('valid')
        else:   # 어 근데 다 채워서 무승부인 경우도 있음 이거 처리
            if win_o(O_idx):
                print('invalid')
            else:
                print('valid')
    elif X_num == O_num:  # O가 이길 수 있음
        if win_o(O_idx):
            print('valid')
        else:
            print('invalid')
    elif X_num < O_num or (X_num - O_num) > 1:
        print('invalid')
#
# _XX
# X_X
# OOO


