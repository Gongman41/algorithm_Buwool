def dp(n):
    tmp = [1, 2]
    for i in range(1, n):
        p2 = tmp[1]

        tmp[1] = (tmp[0] + tmp[1])%15746
        tmp[0] = p2
    
    return tmp[0]
N = int(input())
print(dp(N))