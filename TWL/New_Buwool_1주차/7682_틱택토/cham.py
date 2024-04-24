import sys
sys.stdin = open('input.txt')

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
        else:
            X_num += 1
            X_idx.append(i)
    if abs(O_num - X_num) > 1:  # 각 팀의 말 개수 차이가 2 이상이면
        print('invalid')
        break
    elif O_num < 3 and X_num < 3:   # 각 팀의 말 개수가 3개가 안되면
        print('invalid')
        break

