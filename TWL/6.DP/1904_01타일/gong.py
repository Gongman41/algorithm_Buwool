# N이 짝수일때 00이 N//2번까지, 홀수일떄도 N//2번이긴 함 N-1  N-3 ... N-N
# N(N/2)-N(N+1)/4 
# 1 or 00

def fib(n):
    # if n == 1:
    #     return 1
    # elif n==2:
    #     return 2
    # else:
    #     return fib(n-1) + fib(n-2)
    # 재귀 깊이 문제
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, (a + b) % 15746
    return a


    


import math
N = int(input())


# N이 1 또는 2일 때는 예외 처리
# if N == 1:
#     print(1)
# elif N == 2:
#     print(2)
# else:
    
print(fib(N))
    # count = 1
    # cur = N // 2  
    
    # for i in range(1, cur + 1):
    #     count += math.factorial(N - i) // (math.factorial(i) * math.factorial(N - 2 * i))
    
    # print(count % 15746)
    # 이걸로 해보니 N-2일때 값과 N-1일때 값을 더한게 N일때의 값. 즉 피보나치
    # 근데 어떻게 구현하지

    
        