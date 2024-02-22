import sys
sys.stdin = open('input.txt')
N = int(input())
check = '369'
for n in range(1,N+1):
    st_n = str(n)
    clap_n = 0
    for s in st_n:
        if s in check:
            clap_n += 1
    if clap_n == 0:
        print(st_n, end=' ')
    else:
        print(f'{"-"*clap_n}',end=' ')


