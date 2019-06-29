from collections import defaultdict


def solution(letter, news_paper):
    count = defaultdict(int)

    for char in news_paper:
        count[char] += 1

    for char in letter:
        if char not in count:
            return False

    return True
