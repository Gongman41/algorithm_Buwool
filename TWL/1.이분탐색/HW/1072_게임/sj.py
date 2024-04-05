x, y = map(int, input().split())

original = y * 100 // x

start = 1
end = x
result = 1000000001

while start <= end:
    middle = (start + end) // 2
    z = (y + middle) * 100 // (x + middle)

    if z == original:
        start = middle + 1
    elif z > original:
        result = middle
        end = middle - 1

if end == x:
    result = -1
print(result)
