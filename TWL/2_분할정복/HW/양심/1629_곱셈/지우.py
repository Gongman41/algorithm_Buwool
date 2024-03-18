def tt(a, b):
    if b == 1:
        return a%c
    else:
        if b%2 == 0:
            tmp = tt(a, b//2)
            return tmp * tmp % c
        else:
            tmp = tt(a, (b-1)//2)
            return tmp * tmp * a % c

a, b, c = map(int, input().split())
print(tt(a, b))
'''
2**6
== 2**3 * 2**3
(2**2)**3
2**7
2**6 *2
2**2 * 2**2 * 2**2 * 2
(2**2)**3 * 2

'''