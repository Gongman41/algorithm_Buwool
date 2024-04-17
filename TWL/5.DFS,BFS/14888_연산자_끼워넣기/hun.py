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


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
results = []
generate_expressions(nums, operators, [''] * (N - 1), 0, N - 1, results)
print(max(results))
print(min(results))
