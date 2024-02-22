import sys
sys.stdin = open('input.txt')

K = int(input())

total_area = 1
area = []
d_direc = []

minus_area = 0

for _ in range(6):
    d, m = map(int, input().split())
    if not area:
        area.append((d, m))
    else:
        if d == 1:
            if area[-1][0] != 3:
                minus_area = m * area[-1][1]
                d_direc = (d, area[-1][0])
        elif d == 2:
            if area[-1][0] != 4:
                minus_area = m * area[-1][1]
                d_direc = (d, area[-1][0])
        elif d == 3:
            if area[-1][0] != 2:
                minus_area = m * area[-1][1]
                d_direc = (d, area[-1][0])
        elif d == 4:
            if area[-1][0] != 1:
                minus_area = m * area[-1][1]
                d_direc = (d, area[-1][0])
        area.append((d, m))

if not minus_area:
    minus_area = area[0][1] * area[-1][1]
    d_direc = (area[0][0], area[-1][0])

for i in area:
    if i[0] not in d_direc:
        total_area *= i[1]

total_area -= minus_area

print(total_area*K)