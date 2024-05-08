import sys

n = int(input())

endPoint = 0
cnt = 0

arr = []

for i in range(n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])

# 일찍 끝나는 거부터 정렬해서 그거부터 하면 됨
arr.sort(key=lambda x: (x[1], x[0]))

for newStart, newEnd in arr:
    if endPoint <= newStart:
        cnt += 1
        endPoint = newEnd
print(cnt)