from collections import deque


def reverse(node1, node2, is_right=True):
    left = node1.left
    right = node1.right
    node1.right = node2.right
    node1.left = node2.left

    if is_right:
        node2.right = node1
        node2.left = left
    else:
        node2.left = node1
        node2.right = right

    return node2


def heapify(node):
    # basic idea... if one of it's children is less, swap self, what if both are less? pick any
    # let me first populate the right or the left empty node if possible
    if node is None:
        pass

    if node.right.value < node.value:
        new_node = reverse(node, node.right)
        heapify(new_node.right)
    elif node.left.value < node.value:
        new_node = reverse(node, node.left, False)
        heapify(new_node.left)


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent


class Heap:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        processQueue = deque([self.root])

        while True:
            try:
                currentNode = processQueue.popleft()
                # populate leafs with new node if appropriate
                if node.value > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = node
                        node.parent = currentNode
                    elif currentNode.left is None:
                        currentNode.left = node
                        node.parent = currentNode
                    # add new nodes to be processed
                    elif node.value > currentNode.right.value:
                        processQueue.append(currentNode.right)
                    elif node.value > currentNode.left.value:
                        processQueue.append(currentNode.left)
                else:
                    parent = currentNode.parent
                    node.parent = parent
                    node.right = currentNode
                    currentNode.parent = node

                    if self.root is currentNode:
                        self.root = node

            except IndexError:
                break

    def take_top(self):
        if self.root:
            value = self.root.value
            if self.root.right and self.root.left:
                if self.root.right.value < self.root.left.value:
                    right = self.root.right
                    left = self.root.left
                    self.root = right
                    self.insert(left)
                else:
                    left = self.root.left
                    right = self.root.right
                    self.root = left
                    self.insert(right)
            else:
                self.root = self.root.right if self.root.right else self.root.left
            return value
        else:
            return None


def solution(n):
    """
    n is a list of lists, each list is sorted, we need to produce on final sorted list
    1. brute force is to concat them an sort
    2. better solution is to exploit the fact that lists are sorted, we can then use min-heap
    to only maintain  in memory k items (k is number of lists)... nice
    let me implement min-heap quickly :D
    """
    heap = [-1] * len(n)
    index = 0
    max_len = 0
    for l in n:
        max_len = max(max_len, len(l))
        heap[index] = l[0]
        index += 1

    heapify(heap)

    final_list = [take_min(heap)]
    index = 1
    next_batch = [0] * len(n)

    while index < max_len:
        next_batch_index = 0
        for l in n:
            if index < len(l):
                next_batch[next_batch_index] = l[index]
                next_batch_index += 1

        next_batch.sort()

        for number_index in range(next_batch_index):
            insert(heap, next_batch[number_index])
            final_list.append(take_min(heap))
        index += 1

    [final_list.append(item) for item in heap[1:]]
    return final_list


def insert(heap, item):
    heap[0] = item
    heapify(heap)


def take_min(heap):
    return heap[0]


def heapify(heap):
    index = 1
    while index < len(heap):
        if heap[index] < heap[index - 1]:
            heap[index], heap[index - 1] = heap[index - 1], heap[index]
        index += 1


def solution2():
    # use python built in heap, but then I can just put numbers in and take out? yes
    #but it wont be performing, so I will then do the same trick I do above, process batches of three
    pass


"""
Why am I angry? Its just deep work, its just overcoming resistance, nothing else
things to fix- how can I insert more than one element and heapify on each insert? (insert is the big question)
for example [1,2,3] now insert 0, [0, 1, 2, 3], 2 ? [1,2,3] -> [1,2,2,3]
is it easier to represent this wtih trees? I need to work it out on paper, how to insert a node in a heap tree
and then heapify it... (I think it is easier, jut append it to the end of the tree and let is swap places until its 
parent is less then it...)... I can do that with array then
how? well what when the array is full? the problem is I need the last nodes, I don't need the top ones.. So it would be
better if I can remove the top node and insert from the top... hell yeah.. take the top node. then keep swapping the new
elem until I find it's place.. But I have to extend the size to n*2.. When I insert a new node. what guarantees me that 
it will not remove nodes that I need? because when I swap I don't remove anything.. so I wont lose nodes but I also 
can't insert more nodes in that way... since inserting requires me to remove the head... 
This means that I have a bug in this implementation... 
let me think about what it means to have all input array sorted... 
so should I persue a tree implementation or fix this array implementation?
what is stopping me from using an array implementation? well, I need two ways of inserting elements,
from back and from top, why?
 well because when I array is not filled I can insert from the back and then heapify the array... 
if its full take the head and insert on top, then heapify... but that would mean I can't insert
more then one item, which I need... well I can perfrom one optimization to fix this implementation,
I can sort the next three inputs and then insert them in... well it works up until a point... 
why? well because when I have three sequences I can have the smallest numbers in the end, and for
that to work I need a bigger size of the heap, I can't just have k size array... let me read in the
book again how they are doing it...
I am giving up on the array part, why? well because I want to avoid growing and shrinking arrays.. well
I can just set a bigger array size so I don't have to resize it... what is the minimum size? 
"""
