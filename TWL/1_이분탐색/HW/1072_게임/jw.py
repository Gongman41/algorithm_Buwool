from math import trunc
X, Y = map(int, input().split())
Z = trunc(100*Y/X)
'''
파이썬 실수 자료형 소숫점 오류 ?
'''
if Z >= 99:
    print(-1)
else:
    start = 1
    end = X
    while start <= end:
        mid = (start+end)//2
        if Z == trunc(100*(Y+mid)/(X+mid)):
            start = mid+1
        elif Z < trunc(100*(Y+mid)/(X+mid)):
            end = mid-1
        else:
            break
    print(start)