import sys
sys.stdin = open('input.txt')

lst = []
for _ in range(9):
    key = int(input())
    lst.append(key)
for num_1 in lst:
    for num_2 in lst:
        if num_1 != num_2 and sum(lst) - num_1 - num_2 == 100:
            lst.remove(num_1)
            lst.remove(num_2)
            break
lst.sort()
for number in lst:
    print(number)