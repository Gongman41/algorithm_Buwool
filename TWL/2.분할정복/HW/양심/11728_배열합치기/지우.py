N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = b = 0
result = []
while a < N and b < M:
    if A[a] <= B[b]:
        result.append(A[a])
        a += 1
    else:
        result.append(B[b])
        b += 1

while a < N:
    result.append(A[a])
    a += 1

while b < M:
    result.append(B[b])
    b += 1

print(*result)


    