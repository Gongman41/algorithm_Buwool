'''
수열에서 가장 긴 부분 수열이 나오려면~~??
수열에서 가장 긴 ...
부분 수열
각 각 칸을 이동하면 최댓값을 적어두고 더큰 숫자가 나올때 마다 최댓값을 갱신을 해준다.
이게 되려나
'''
N = int(input())
arr = list(map(int, input().split()))
# print(arr)
result_lst = [1] * N

for i in range(N):
    result_lst[i] = 