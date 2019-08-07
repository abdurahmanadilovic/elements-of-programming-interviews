from random import randint


def solution(array, size):
    for index in range(size):
        picked_index = randint(index, len(array) - 1)
        array[index], array[picked_index] = array[picked_index], array[index]

    return array

