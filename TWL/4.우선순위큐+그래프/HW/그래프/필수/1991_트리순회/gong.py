import sys
sys.stdin = open('input.txt')

def post(cur):

    print(babies[cur][0],end='')
    if babies[cur][1] != '.':
        post(babies[cur][1])
    if babies[cur][2] != '.':
        post(babies[cur][2])
def mid(cur):

    if babies[cur][1] != '.':
        mid(babies[cur][1])
    print(babies[cur][0],end='')
    if babies[cur][2] != '.':
        mid(babies[cur][2])


def last(cur):

    if babies[cur][1] != '.':
        last(babies[cur][1])
    if babies[cur][2] != '.':
        last(babies[cur][2])
    print(babies[cur][0],end='')


N = int(input())
babies = {}
for i in range(N):
    p,b1,b2 = input().split()
    babies[p] = [p,b1,b2]
    # ord(A) == 65
post('A')
print()
mid('A')
print()
last('A')