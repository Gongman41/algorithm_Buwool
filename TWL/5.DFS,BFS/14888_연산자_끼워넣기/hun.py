# N = int(input())
# lst = list(map(int, input().split()))
# pls, mis, gob, div = map(int, input().split())  # + - * //
# max_num = -1e9
# min_num = 1e9
#
#
# def check():
#     global max_num, min_num, pls, mis, gob, div
#     if

import sys

def calculate_expression(nums, operators):
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i+1]
        elif operators[i] == '-':
            result -= nums[i+1]
        elif operators[i] == '*':
            result *= nums[i+1]
        elif operators[i] == '/':
            # Integer division
            if result < 0:
                result = -(-result // nums[i+1])
            else:
                result //= nums[i+1]
    return result

def generate_expressions(nums, operators, used_operators, depth, max_depth, results):
    if depth == max_depth:
        result = calculate_expression(nums, used_operators)
        results.append(result)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            used_operators[depth] = '+-*/'[i]
            generate_expressions(nums, operators, used_operators, depth + 1, max_depth, results)
            operators[i] += 1

def main():
    # 입력
    N = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    # 식의 결과를 저장할 리스트
    results = []

    # 재귀 함수를 통해 모든 가능한 식을 생성하고 결과 계산
    generate_expressions(nums, operators, [''] * (N - 1), 0, N - 1, results)

    # 결과 출력
    print(max(results))
    print(min(results))

if __name__ == "__main__":
    main()
