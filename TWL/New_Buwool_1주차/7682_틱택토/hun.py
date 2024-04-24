import sys
sys.stdin = open('input.txt')

def bingo_x(lst):
    # 빙고 조건을 검사하는 함수
    return (
        (lst[0] == lst[1] == lst[2] == 'X') or
        (lst[3] == lst[4] == lst[5] == 'X') or
        (lst[6] == lst[7] == lst[8] == 'X') or
        (lst[0] == lst[3] == lst[6] == 'X') or
        (lst[1] == lst[4] == lst[7] == 'X') or
        (lst[2] == lst[5] == lst[8] == 'X') or
        (lst[0] == lst[4] == lst[8] == 'X') or
        (lst[2] == lst[4] == lst[6] == 'X')
    )


def bingo_o(lst):
    # 빙고 조건을 검사하는 함수
    return (
        (lst[0] == lst[1] == lst[2] == 'O') or
        (lst[3] == lst[4] == lst[5] == 'O') or
        (lst[6] == lst[7] == lst[8] == 'O') or
        (lst[0] == lst[3] == lst[6] == 'O') or
        (lst[1] == lst[4] == lst[7] == 'O') or
        (lst[2] == lst[5] == lst[8] == 'O') or
        (lst[0] == lst[4] == lst[8] == 'O') or
        (lst[2] == lst[4] == lst[6] == 'O')
    )
def check(lst):
    cnt_x = lst.count('X')
    cnt_o = lst.count('O')
    if cnt_x == cnt_o or cnt_x == cnt_o + 1:
        if bingo_x(lst) == True and bingo_o(lst) == False:
            if cnt_x == cnt_o:
                print('invalid')
            else:
                print('valid')
        elif bingo_o(lst) == True and bingo_x(lst) == False:
            if cnt_x == cnt_o:
                print('valid')
            else: 
                print('invalid')
        else:
            if cnt_x == 5 or cnt_o == 4:
                if bingo_o(lst) == False and bingo_x(lst) == False:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')   
    else:
        print('invalid')

        

while True:
    lst = list(input())
    # print(lst)
    if len(lst) == 3:
        break
    check(lst)
    # print(bingo_x(lst))
    # print(bingo_o(lst))