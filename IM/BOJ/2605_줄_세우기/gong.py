import sys
sys.stdin = open('input.txt')
N = int(input())
ins_lst = list(map(int,input().split()))
result_lst = []
for n in range(1,N+1):
    result_lst.insert(ins_lst[n-1],n)
print(*result_lst[::-1])
    
    
    