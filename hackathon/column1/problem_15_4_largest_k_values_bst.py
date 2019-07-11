class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0


def solution(root, k):
    return dfs_post_order(root, k)


def dfs_post_order(root, k):
    queue = [root]
    k_list = []

    while len(queue) > 0:
        top = queue.pop()

        if top.right is None and top.left is None:
            k_list.append(top.value)

            if len(k_list) == k:
                return k_list

            continue

        if top.left:
            queue.append(top.left)

        topCopy = Node()
        topCopy.value = top.value
        queue.append(topCopy)

        if top.right:
            queue.append(top.right)
