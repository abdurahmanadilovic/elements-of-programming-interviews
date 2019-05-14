def solution(n):
    if len(n) == 0:
        return 0

    maximum = [0] * len(n)
    current_max = n[-1]

    for index in range(len(n)-1, -1, -1):
        current_max = max(current_max, n[index])
        maximum[index] = current_max

    maximum_profit = maximum[0] - n[0]

    for index in range(len(n)):
        maximum_profit = max(maximum_profit, maximum[index] - n[index])

    return maximum_profit


def solution2(n):
    if len(n) == 0:
        return 0

    minimum = n[0]
    max_profit = 0

    for item in n:
        max_profit = max(max_profit, item - minimum)
        minimum = min(minimum, item)

    return max_profit


def solution_variant(n):
    """
    given an integer array find the maximum sub array of values that are the same...
    easy... Use two pointers, keep growing as long as items are the same, when
    they are not, capture its length and compare it to the maximum so far
    """
    left, right = 0, 0
    maximum_length = 0

    while left < len(n):
        right = left + 1

        while right < len(n) and n[right] == n[left]:
            right += 1

        if n[left] == n[left + 1]:
            maximum_length = max(maximum_length, right - left)

        left = right

    return maximum_length

