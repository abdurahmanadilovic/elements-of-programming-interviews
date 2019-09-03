def solution(cities):
    carry = 0
    min_city = [0, 0]

    for index in range(1, len(cities)):
        carry += cities[index - 1][0] - cities[index - 1][1]
        if carry < min_city[1]:
            min_city = [index, carry]

    return min_city[0]
