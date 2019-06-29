from collections import defaultdict


def solution(letter, news_paper):
    news_paper_count = defaultdict(int)
    letter_count = defaultdict(int)

    for char in news_paper:
        news_paper_count[char] += 1

    for char in letter:
        letter_count[char] += 1

    for key in letter_count:
        if letter_count[key] != news_paper_count[key]:
            return False

    return True
