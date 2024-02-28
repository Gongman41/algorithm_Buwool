# import sys
# sys.stdin = open("input.txt", "r")

switch = int(input())
status = list(map(int, input().split()))
status.insert(0, 0)
student = int(input())
for s in range(student):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(switch + 1):
            if i%number == 0:
                status[i] = 1 - status[i]
    if gender == 2:
        j = 0
        while j < min(number, switch-number+1) and status[number+j] == status[number-j]:
            j += 1
        status[number] = 1 - status[number]
        for k in range(1, j):
            status[number + k] = 1 - status[number + k]
            status[number - k] = 1 - status[number - k]
for s in range(1, switch + 1):
    print(status[s], end=' ')
    if s % 20 == 0:
        print()