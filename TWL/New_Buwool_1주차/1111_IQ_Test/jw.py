N = int(input())
num = list(map(int, input().split()))

if N <= 2:
    if N == 2 and num[0] == num[1]:
        print(num[0])
    else:
        print('A')
else:
    x, y, z = num[:3]
    if x == y:
        for i in range(2, N):
            if num[i] != x:
                exit(print('B'))
        else:
            exit(print(x))

    if y == z:
        for i in range(3, N):
            if num[i] != y:
                exit(print('B'))
        else:
            exit(print(y))

    for a in range(-200, 200):
        nx = x * a
        b = y - nx
        if z != y * a + b:
            continue
        nz = z
        for i in range(3, N):
            if num[i] == nz * a + b:
                nz = nz * a + b
            else:
                break
        else:
            exit(print(nz * a + b))
    print('B')