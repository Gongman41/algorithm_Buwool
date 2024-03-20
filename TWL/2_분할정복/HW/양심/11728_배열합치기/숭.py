def merge_sort(unordered):
    if len(unordered) <= 1:
        return unordered

    middle = len(unordered) // 2
    left = unordered[:middle]
    right = unordered[middle:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)

    return merge(left_, right_)

def merge(left, right):
    i = j = 0
    sorted = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    while i < len(left):
        sorted.append(left[i])
        i += 1
    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted

n, m = map(int, input().split())
n_array = list(map(int, input().split()))
m_array = list(map(int, input().split()))

unordered_list = (n_array + m_array)

print(' '.join(map(str, merge_sort(unordered_list))))