class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def set_value(self, data):
        self.data = data


def solution(a, b):
    head = Node()
    current = head

    while a is not None and b is not None:
        if a.get_data() < b.get_data():
            current.set_next(a)
            a = a.get_next()
        else:
            current.set_next(b)
            b = b.get_next()

        current = current.get_next()

    rest = a if a is not None else b

    current.set_next(rest)

    return head.get_next()


a = Node(10)
b = Node(9, a)
c = Node(8, b)

h = Node(12)
g = Node(11, h)
f = Node(7, g)
e = Node(4, f)

head = solution(c, e)

while head is not None:
    print(head.get_data())
    head = head.get_next()
