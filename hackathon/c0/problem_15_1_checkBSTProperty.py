class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0


def is_less_than_max(value, max_value):
    return value < max_value if max_value != -1 else True


def is_bst(node, min_value, max_value):
    if node is None:
        return True
    if min_value < node.value and is_less_than_max(node.value, max_value):
        left_ok = is_bst(node.left, min_value, node.value)
        if not left_ok:
            return left_ok
        else:
            return is_bst(node.right, node.value, max_value)
    else:
        return False


def solution(root):
    left_ok = is_bst(root.left, 0, root.value)
    if not left_ok:
        return left_ok
    else:
        return is_bst(root.right, root.value, -1)



