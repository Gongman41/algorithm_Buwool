import sys
sys.stdin = open('input.txt')

def back(i, sum, lst):
    global result
    if result:
        return
    if len(lst) > 7:
        return
    elif i == 9:
        if len(lst) == 7 and sum == 100:
            result = lst
            return
        else:
            return
    elif len(lst) == 7:
        if sum == 100:
            result = lst
            return
        else:
            return
    elif sum > 100:
        return
    else:
        back(i+1, sum + arr[i], lst + [arr[i]])
        back(i+1, sum, lst)

arr = [int(input()) for _ in range(9)]
result = []
back(0, 0, [])
result.sort()
print(*result, sep = '\n')
