from collections import defaultdict


class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value


def get_height(node):
    height = 0

    while node is not None:
        height += 1
        node = node.parent

    return height


def solution2(node1, node2):
    height1, height2 = get_height(node1), get_height(node2)

    node_to_correct = node1

    if height1 < height2:
        node_to_correct = node2

    diff = abs(height1 - height2)

    while diff > 0:
        node_to_correct = node_to_correct.parent
        diff -= 1

    if height1 < height2:
        node2 = node_to_correct
    else:
        node1 = node_to_correct

    while node1.parent != node2.parent:
        node1 = node1.parent
        node2 = node2.parent

    return node1.parent


# less efficient, takes O(n) space
def solution(node1, node2):

    visited = defaultdict(bool)

    while True:
        if node1 and node1.parent:
            if visited[node1.parent.value]:
                return node1.parent
            visited[node1.parent.value] = True

        if node2 and node2.parent:
            if visited[node2.parent.value]:
                return node2.parent

            visited[node2.parent.value] = True

        node1 = node1.parent
        node2 = node2.parent
