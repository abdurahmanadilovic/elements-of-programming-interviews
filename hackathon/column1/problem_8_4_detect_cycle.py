class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def solution(root):
    slow_iterator = root
    fast_iterator = root.next

    while fast_iterator is not None:
        slow_iterator = slow_iterator.next
        fast_iterator = fast_iterator.next.next

        if slow_iterator == fast_iterator:
            # we have a cycle
            cycle_length = 0
            fast_iterator = fast_iterator.next

            while fast_iterator != slow_iterator:
                cycle_length += 1
                fast_iterator = fast_iterator.next

            first_iterator = root
            second_iterator = root

            while cycle_length > 0:
                second_iterator = second_iterator.next
                cycle_length -= 1

            while True:
                second_iterator = second_iterator.next

                if first_iterator == second_iterator:
                    return first_iterator

                first_iterator = first_iterator.next

    return None

