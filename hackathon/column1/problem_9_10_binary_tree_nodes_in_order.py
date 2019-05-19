from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def solution(root):
    solution_array = [[1]]

    parentQueue = deque([root])

    while len(parentQueue) > 0:
        children = []
        values = []

        while len(parentQueue) > 0:
            parentNode = parentQueue.pop()

            if parentNode.left and parentNode.right:
                children.append(parentNode.left)
                children.append(parentNode.right)

                values.append(parentNode.left.value)
                values.append(parentNode.right.value)

        if len(values) > 0:
            solution_array.append(values)

        parentQueue.extend(children)

    return solution_array
