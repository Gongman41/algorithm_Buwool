import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
data = list(input().strip())
result = -int(1e9)

def calculate(a, oper, b):
    if oper == '+':
        num = a + b
    elif oper == '*':
        num = a * b
    elif oper == '-':
        num = a - b
    return num

def dfs(index, value):
    global result

    if index == N - 1:
        result = max(result, value)
        return

    if index + 2 < N:
        next_value = calculate(value, data[index + 1], int(data[index + 2]))
        dfs(index + 2, next_value)

    if index + 4 < N:
        next_next_value = calculate(int(data[index+2]), data[index+3], int(data[index+4]))
        next_value = calculate(value, data[index + 1], next_next_value)
        dfs(index + 4, next_value)

dfs(0, int(data[0]))

print(result)