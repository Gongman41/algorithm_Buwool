import sys
N = int(sys.stdin.readline())
timeline = []
for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    timeline.append((start, end))

timeline.sort(key=lambda x : (x[1],x[0]))
count = 1
end = timeline[0][1]
for i in range(1, N):
    if timeline[i][0]>=end:
        end = timeline[i][1]
        count += 1

print(count)