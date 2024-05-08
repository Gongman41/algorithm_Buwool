import sys
sys.setrecursionlimit(10**6)


def is_integer(s):
    try:
        s = int(s)
        return s

    except ValueError:
        return 'op'


def sel(idx, exp, prev):
    if idx > N-1:
        cal(exp)
        return
    now = is_integer(ex[idx])
    if now != 'op':
        # 숫자
        sel(idx+1, exp + [now], 0)
    else:
        # 연산자
        op = ex[idx]
        sel(idx+1, exp + [op], 0)
        if not prev:
            a = exp.pop()
            b = int(ex[idx+1])
            if op == '+':
                tmp = a + b
            elif op == '-':
                tmp = a - b
            else:
                tmp = a * b

            sel(idx+2, exp + [tmp], 1)

    '''
        숫자면 그냥 넣고
        연산자면 그냥 연산자 넣기
        or exp 마지막 값 pop -> ex[idx+1] 이랑 계산한 숫자 넣고 idx + 2로

        전에 괄호 넣었으면 다음에 못넣음
    '''


def cal(exp):
    global result
    # 계산하고 갱신
    stack = []
    l = len(exp)
    for i in range(l):
        now = is_integer(exp[i])
        if now != 'op':
            if i == 0:
                stack.append(exp[i])
            else:
                op = stack.pop()
                a = stack.pop()
                if op == '+':
                    tmp = a + now
                elif op == '-':
                    tmp = a - now
                else:
                    tmp = a * now
                stack.append(tmp)
        else:
            stack.append(exp[i])

    if result < stack[0]:
        result = stack[0]


N = int(input())
ex = list(input().strip())
result = -1e9
sel(0, [], 0)

print(result)
'''
    우선순위 같음, 왼쪽부터 계산
    스택

    괄호 최대 N//2개
    완탐
'''
