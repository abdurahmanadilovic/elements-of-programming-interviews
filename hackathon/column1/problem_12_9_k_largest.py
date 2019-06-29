from random import randint


def partition_around_index(left, right, index, array):
    value = array[index]
    leftPosition = left
    array[right], array[index] = array[index], array[right]

    for index in range(left, right):
        if array[index] < value:
            array[index], array[leftPosition] = array[leftPosition], array[index]
            leftPosition += 1

    array[right], array[leftPosition] = array[leftPosition], array[right]

    return leftPosition


def solution(array, k):
    left = 0
    right = len(array) - 1

    while left <= right:
        randIndex = randint(left, right)
        newIndex = partition_around_index(left, right, randIndex, array)

        if newIndex == k - 1:
            return array[newIndex]
        elif newIndex < k - 1:
            left = newIndex + 1
        else:
            right = newIndex - 1
