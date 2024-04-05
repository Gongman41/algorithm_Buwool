import sys
input = sys.stdin.readline

N = int(input())
sc = list(map(int, input().split()))
M = int(input())
fc = list(map(int, input().split()))


dic = {}
for i in sc:
    if i in dic:
        dic[i] += 1
    else: dic[i] = 1

print(' '.join(str(dic[i]) if i in dic else '0' for i in fc))

'''
얘는 pypy도 안됨
왜 ?

dic = {}
for i in sc:
    if i in dic:
        dic[i] += 1
    else: dic[i] = 1

ans = ''
for i in fc:
    if i in sc: ans += str(dic[i])
    else: ans += '0'
    ans += ' '

print(ans)
'''

''' pypy로는 되네
sc.sort()
l = []
r = []

for c in fc:
    s = 0
    e = N-1
    if sc[s] <= c <= sc[e]:
        while s <= e:
            m = (s+e)//2
            if sc[m] < c:
                s = m+1
            
            else:
                e = m-1
                
        if sc[s] == c:
            l.append(s)
        else: l.append(0)
    else:
        l.append(0)

for c in fc:
    s = 0
    e = N-1
    if sc[s] <= c <= sc[e]:
        while s <= e:
            m = (s+e)//2
            if sc[m] > c:
                e = m-1
            
            else:
                s = m+1
                
        if sc[e] == c:
            r.append(e+1)
        else: r.append(0)
    else:
        r.append(0)

for i in range(M):
    print(r[i]-l[i], end=' ')
'''
