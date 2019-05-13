def solution(numbers=[], target=0):
    numbers.sort()
    for number in numbers:
        if twoSum(numbers, target - number):
            return True

    return False


def twoSum(numbers=[], target=0):
    i, j = 0, len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return True
        elif sum < target:
            i += 1
        else:
            j -= 1
    return False
