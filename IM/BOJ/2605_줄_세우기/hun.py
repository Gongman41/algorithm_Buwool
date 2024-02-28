import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
new_lst = []
for i in range(N):
    new_lst.insert(i-lst[i], i)
for num in new_lst:
    print(num+1, end=' ')