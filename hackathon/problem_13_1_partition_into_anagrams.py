from collections import defaultdict


def solution(n):
    table = defaultdict(list)
    for string in n:
        table[''.join(sorted(string))].append(string)

    res = []
    for key in table:
        if len(table[key]) > 1:
            res.extend(table[key])

    return res
