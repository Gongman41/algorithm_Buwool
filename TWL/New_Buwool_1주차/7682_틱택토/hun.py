# '''
# 처음은 반드시 x 가 먼저 놓는다
# --> x 갯수랑 o 갯수랑 차이가 2이상이 될수 없다
# --> o 갯수가 많을 수 없다
# --> x 랑 o 가 둘다 빙고인 경우는 나올 수 가 없다
# --> x만 빙고, o 빙고 아님 가능 
# --> x가 두개가 빙고가 나올수 있는 경우(생각할 필요 없다)

# xxx
# oo.
# xxx
# -> invalid

# xox
# oxo
# xox
# -> valid

# oxo
# xox
# oxo
# -> invalid

# xxo
# oox
# xox
# -> valid

# xo.
# ox.
# ..x
# -> valid

# .xx
# x.x
# ooo
# -> invalid

# x.o
# o..
# x..
# -> valid

# oox
# xxo
# oxo
# -> invalid
# '''

import sys
sys.stdin = open('input.txt')

def bingo(lst):
    # 빙고 조건을 검사하는 함수
    if lst[0] == lst[1] == lst[2]:
        if lst[0] == 'X':
            return 'bingo_x'
    elif lst[3] == lst[4] == lst[5]:
        return True    
    elif lst[6] == lst[7] == lst[8]:
        return True    
    elif lst[0] == lst[3] == lst[6]:
        return True    
    elif lst[1] == lst[4] == lst[7]:
        return True    
    elif lst[2] == lst[5] == lst[8]:
        return True    
    elif lst[0] == lst[4] == lst[8]:
        return True    
    elif lst[2] == lst[4] == lst[6]:
        return True    
    return False

def check(lst):
    # X와 O의 개수를 세고, 빙고 상태를 확인하여 유효성을 판별하는 함수
    cnt_x = lst.count('X')
    cnt_o = lst.count('O')
    
    if cnt_x - cnt_o == 1 or cnt_x - cnt_o == 0:
        if bingo(lst):
            print('valid')
            return
    print('invalid')

        

while True:
    lst = list(input())
    # print(lst)
    if len(lst) == 3:
        break
    check(lst)



# import sys
# sys.stdin = open('input.txt')

# def is_valid(board):
#     # X와 O의 개수를 세는 변수
#     count_x = 0
#     count_o = 0
    
#     # 빙고 개수를 세는 변수
#     bingo_x = 0
#     bingo_o = 0
    
#     # 가로, 세로, 대각선에 대한 빙고를 검사하는 함수
#     def check_bingo(lst):
#         if lst[0] == lst[1] == lst[2] and lst[0] != '.':
#             return True
#         return False
    
#     # 보드의 각 행, 열, 대각선에 대해 검사
#     for i in range(3):
#         # 가로 검사
#         if check_bingo(board[i*3:i*3+3]):  # 각 행에 대해 가로 빙고 검사
#             if board[i*3] == 'X':
#                 bingo_x += 1
#             elif board[i*3] == 'O':
#                 bingo_o += 1
                
#         # 세로 검사
#         if check_bingo([board[i], board[i+3], board[i+6]]):  # 각 열에 대해 세로 빙고 검사
#             if board[i] == 'X':
#                 bingo_x += 1
#             elif board[i] == 'O':
#                 bingo_o += 1
                
#     # 대각선 검사
#     if check_bingo([board[0], board[4], board[8]]):  # 왼쪽 위에서 오른쪽 아래로의 대각선
#         if board[0] == 'X':
#             bingo_x += 1
#         elif board[0] == 'O':
#             bingo_o += 1
#     if check_bingo([board[2], board[4], board[6]]):  # 오른쪽 위에서 왼쪽 아래로의 대각선
#         if board[2] == 'X':
#             bingo_x += 1
#         elif board[2] == 'O':
#             bingo_o += 1
    
#     # X와 O의 개수 세기
#     for i in board:
#         if i == 'X':
#             count_x += 1
#         elif i == 'O':
#             count_o += 1
            
#     # 조건에 맞게 유효성 판별
#     if (count_x == count_o + 1 and bingo_x == 1 and bingo_o == 0) or (count_x == count_o and bingo_x == 0 and bingo_o == 0):
#         return "valid"
#     else:
#         return "invalid"

# # 입력 받기
# while True:
#     board = input()
#     if board == "end":
#         break
#     print(is_valid(board))

