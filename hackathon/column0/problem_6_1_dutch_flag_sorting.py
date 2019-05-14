def solution2(n, i):
    """
    given an index i, sort  the array such that elements less then i appear before i
    then element at i, then all items that are larger
    """
    left = [0] * len(n)
    right = [0] * len(n)
    pivot = n[i]

    i, li, ri = 0, 0, 0

    while i < len(n):
        if n[i] < pivot:
            left[li] = n[i]
            li += 1
        if n[i] > pivot:
            right[ri] = n[i]
            ri += 1
        i += 1

    i, j, k = 0, 0, 0

    while i < len(n):
        while j < li:
            n[i] = left[j]
            j += 1
            i += 1
        n[i] = pivot
        i += 1
        while k < ri:
            n[i] = right[k]
            k += 1
            i += 1

    return n


def solution3(n, i):
    left, right = 0, len(n) - 1
    pivot = n[i]
    while left < right and left < len(n):
        if n[left] > pivot:
            while right > left and n[right] > pivot:
                right -= 1
            n[right], n[left] = n[left], n[right]
        left += 1

    left, right = 0, len(n) - 1
    while right > left:
        if n[right] < pivot:
            while left < right and n[left] < pivot:
                left += 1
            n[right], n[left] = n[left], n[right]
        right -= 1

    return n


def solution(n, i):
    pivot = n[i]

    swap_index = 0
    for index in range(len(n)):
        if n[index] < pivot:
            n[swap_index], n[index] = n[index], n[swap_index]
            swap_index += 1

    swap_index = len(n) - 1
    for index in range(len(n)-1, -1, -1):
        if n[index] > pivot:
            n[swap_index], n[index] = n[index], n[swap_index]
            swap_index -= 1

    return n
