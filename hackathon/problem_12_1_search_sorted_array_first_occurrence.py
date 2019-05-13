def solution(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k:
            while a[mid] == k:
                mid -= 1
            return mid + 1
        elif a[mid] > k:
            right = mid - 1
        else:
            left = mid + 1


def solution2(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k:
            right = mid - 1
        elif a[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return right+1 if a[right+1] == k else None
