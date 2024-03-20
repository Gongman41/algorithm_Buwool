# import sys
# sys.stdin = open('input.txt')
N,M = map(int,input().split())
n_lst = list(map(int,input().split()))
m_lst = list(map(int,input().split()))
print(*sorted(n_lst+m_lst))