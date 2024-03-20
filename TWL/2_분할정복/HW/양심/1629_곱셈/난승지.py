def sol(a, b, c):
    if b == 1:
        return a % c
    # 어떤 수의 거듭제곱 한 것의 제곱을 곱하며 연산의 횟수를 줄임
    elif b % 2 == 0:
        return (sol(a,b//2,c)**2)%c
    else:
        return ((sol(a,b//2,c)**2)*a)%c

abc = list(map(int, input().split()))
print(sol(abc[0], abc[1], abc[2]))