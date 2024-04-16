N = int(input())


def Fib(N):
    memo = [1, 2]
    for index in range(2, N+1):
        memo.append((memo[index-1] + memo[index-2]) % 15746)
    print(memo[N])
Fib(N-1)


# 피보나치수열

# a = 1
# b = 2
#
# for i in range(1, N):
#     a, b = b, a + b
# print(a)


# lst = [0] * (N+3)
# lst[1] = 1
# lst[2] = 2
# for i in range(N):
#     lst[i+3] = lst[i+1] + lst[i+2]
# print(lst[N] % 15746)
'''
4
00 또는 1 
타일을 이용해서 
만들수 있는 모든 경우를 찾아보시오
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8
6 -> 13

result_1 1 2 3
result_2 2 3 5
'''
