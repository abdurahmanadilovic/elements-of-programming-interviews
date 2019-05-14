def solution(x, y):
    if y < 0:
        x = 1 / x
        y = -y

    result = 1

    while y:
        if y & 1:
            result *= x
        x, y = x * x, y >> 1

    return result
