import sys

n = int(input())
s = input()
result = -1 * sys.maxsize

def myOperator(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2

def dfs(index, value):
    global result

    if index == n - 1:
        result = max(result, value);
        return

    if index + 2 < n:
        dfs(index + 2, myOperator(value, s[index + 1], int(s[index + 2])))

    if index + 4 < n:
        dfs(index + 4, myOperator(value, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4]))))

dfs(0, int(s[0]))
print(result)