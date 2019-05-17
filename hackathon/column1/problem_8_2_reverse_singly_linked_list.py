class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def solution(node):
    curr, prev = node, None

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev
