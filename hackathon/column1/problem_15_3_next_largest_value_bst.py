from sys import maxsize


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0


def iterate(node, value, min_value):
    if node is None:
        min_value

    if node.value > value:
        min_value = min(min_value, node.value)

    if node.left is not None and node.left.value >= value:
        min_value = iterate(node.left, value, min_value)
    else:
        if node.right is not None and node.right.value >= value:
            min_value = iterate(node.right, value, min_value)

    return min_value


def solution(root, value):
    return dfs_post_order(root, value)


def dfs_post_order(root, value):
    queue = [root]
    closest = maxsize

    while len(queue) > 0:
        top = queue.pop()
        if top.value > value:
            closest = min(top.value, closest)

        if top.left and top.left.value >= value:
            queue.append(top.left)
        elif top.right and top.right.value >= value:
            queue.append(top.right)

    return closest
