# 지금 연산자가 들어갈 위치, 연산자의 왼쪽 피연산자, 연산자의 오른쪽 피연산자
def calculate(current_index, before_num, operator_index):
    return operators[operator_index](before_num, array[current_index])

def back_tracking(index, now_sum):
    global max_sum, min_sum
    # 연산자를 넣을 위치가 다 찼다면 sum을 비교하여 원하는 값을 얻어
    if index == n:
        if now_sum > max_sum:
            max_sum = now_sum
        if now_sum < min_sum:
            min_sum = now_sum
        return

    # 연산자가 4개고 operators_cnt의 값을 바꾸며 방문처리를 할 수 있음
    # 같은 연산자가 또 쓸 수도 있으니까 !!
    for i in range(4):
        if operators_cnt[i] > 0:
            operators_cnt[i] -= 1
            back_tracking(index + 1, calculate(index, now_sum, i))
            operators_cnt[i] += 1

# 수의 개수
n = int(input())
# 수들
array = list(map(int, input().split()))
# +, -, *, /의 개수
operators_cnt = list(map(int, input().split()))

# 식의 결과가 최대인 것과 최소인 것을 구해보쟈
max_sum = float('-inf')
min_sum = float('inf')

# 연산자와 그에 알맞게 계산하는 식을 담은 딕셔너리
operators = {0: lambda x,y:x+y, 1: lambda x,y:x-y,
             2: lambda x,y:x*y, 3: lambda x,y:x//y if x>0 else -(-x//y)}

# 연산자가 들어갈 자리를 1~n이라고 할 건데(index)
# 첫번째 자리에 들어가는 순간 바로 앞에 있는 피연산자는 연산의 대상이 되므로 두번째 인자로 넣어줌
back_tracking(1, array[0])

# 결과 출력
print(max_sum, min_sum, sep='\n')
