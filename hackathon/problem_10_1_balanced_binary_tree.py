class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def get_height(root, height):
    if root is None:
        return height
    return max(get_height(root.left, height + 1), get_height(root.right, height + 1))


def is_balanced(root):
    return abs(get_height(root.left, 1) - get_height(root.right, 1)) <= 1


def solution(root):
    left_balanced = is_balanced(root.left)
    right_balanced = False
    if left_balanced:
        right_balanced = is_balanced(root.right)
    return left_balanced and right_balanced


def is_balanced2(root, height):
    """
    optimized version, we stop the first moment a sub tree is not balanced
    """
    if root is None:
        return True, height
    is_left_balanced, height1 = is_balanced2(root.left, height + 1)
    if is_left_balanced is False:
        return False, height
    is_right_balanced, height2 = is_balanced2(root.right, height + 1)
    return abs(height1 - height2) <= 1 and is_right_balanced, max(height1, height2)


def solution2(root):
    is_all_balanced, _ = is_balanced2(root, 0)
    return is_all_balanced



"""
variant return height of the largest subtree that is complete 
"""
