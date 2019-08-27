from functools import lru_cache

"""
operations:
- insert one char
- remove one char
- replace one char
"""


@lru_cache(maxsize=None)
def dp(source, target):
    if source == target:
        return 0

    longest = max(len(source), len(target))

    for index in range(longest):
        if index == len(source) or index == len(target):
            return abs(len(target) - len(source))

        if source[index] != target[index]:
            cost1 = dp(source[index + 1:], target[index + 1:])
            cost2 = dp(source, target[index + 1:])
            cost3 = dp(source[index + 1:], target)
            return 1 + min(cost1, cost2, cost3)

    return 0


def solution(source, target):
    return dp(source, target)
