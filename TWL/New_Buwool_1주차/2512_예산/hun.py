def bin():
    global s, e
    answer = 0
    while s <= e:
        num_sum = 0
        m = (s + e) // 2

        for num in lst:
            num_sum += min(num, m)

        if num_sum <= total:
            s = m + 1
            answer = m
        else:
            e = m - 1

    print(answer)

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = int(input())

s = 0
e = max(lst)
bin()