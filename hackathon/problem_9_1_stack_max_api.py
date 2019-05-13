
class Node:
    def __init__(self, value, previous, max_value):
        self.value = value
        self.previous = previous
        self.max = max_value


class Stack:
    def __init__(self):
        self.__head = None

    def push(self, number):
        if self.__head is None:
            self.__head = Node(number, None, number)
        else:
            current_max = max(self.__head.max, number)
            newNode = Node(number, self.__head, current_max)
            self.__head = newNode

    def pop(self):
        if self.__head is None:
            return None
        else:
            valueToReturn = self.__head.value
            self.__head = self.__head.previous
            return valueToReturn

    def max(self):
        return self.__head.max if self.__head is not None else None


