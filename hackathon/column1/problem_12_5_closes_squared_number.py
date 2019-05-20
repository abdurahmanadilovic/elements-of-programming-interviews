def solution(n):
    high = n
    low = 1

    while low <= high:
        mid = (high + low) // 2
        mid_squared = mid ** 2
        if mid_squared < n:
            low = mid + 1
        if mid_squared > n:
            high = mid - 1
        if mid_squared == n:
            return mid

    return low - 1
