import sys
sys.stdin = open('input.txt')

boy_s = [0]*6
girl_s = [0]*6

N, K = map(int, input().split())

for _ in range(N):
    sex, grade = map(int, input().split())
    if sex == 0:
        girl_s[grade-1] += 1
    else:
        boy_s[grade-1] += 1
# print(girl_s)
# print(boy_s)
cnt = 0
for num in girl_s:
    if num % K == 0:
        cnt += num//K
    else:
        cnt += (num//K + 1)
for num in boy_s:
    if num % K == 0:
        cnt += num//K
    else:
        cnt += (num//K + 1)
print(cnt)
