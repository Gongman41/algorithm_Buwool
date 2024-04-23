'''
처음은 반드시 x 가 먼저 놓는다
--> x 갯수랑 o 갯수랑 차이가 2이상이 될수 없다
--> o 갯수가 많을 수 없다
--> x 랑 o 가 둘다 빙고인 경우는 나올 수 가 없다
--> x만 빙고, o 빙고 아님 가능 
--> x가 두개가 빙고가 나올수 있는 경우

xxx
oo.
xxx
-> invalid

xox
oxo
xox
-> valid

oxo
xox
oxo
-> invalid

xxo
oox
xox
-> valid

xo.
ox.
..x
-> valid

.xx
x.x
ooo
-> invalid

x.o
o..
x..
-> valid

oox
xxo
oxo
-> invalid
'''

def check():
    













cnt = 0
while cnt == 0:
    lst = []
    if input() == 'end':
        cnt += 1
    lst.append(input().split(''))
    print(lst)
