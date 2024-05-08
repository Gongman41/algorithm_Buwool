def cal(a,operator,b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b

def sol(index, sumi):
    global max_sum
    if index == n-1:
        max_sum = max(max_sum, sumi)
        return max_sum
    if index < n-2:
        tmp_sum = cal(sumi, expression[index+1], int(expression[index+2]))
        # 괄호 없는 거
        sol(index+2, tmp_sum)
    if index < n-4:
        tmp_sum = cal(int(expression[index+2]), expression[index+3], int(expression[index+4]))
        # 괄호 있는 거
        sol(index+4, cal(sumi,expression[index+1], tmp_sum))

n = int(input())
expression = list(input())
max_sum = float('-inf')
sol(0, int(expression[0]))
print(max_sum)