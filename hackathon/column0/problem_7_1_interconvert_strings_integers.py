def char_to_int(char):
    if char == '0':
        return 0
    if char == '1':
        return 1
    if char == '2':
        return 2
    if char == '3':
        return 3
    if char == '4':
        return 4
    if char == '5':
        return 5
    if char == '6':
        return 6
    if char == '7':
        return 7
    if char == '8':
        return 8
    if char == '9':
        return 9
    else:
        return -1


def solution(string):
    num = 0
    prev = 0
    decimal = 1
    negative = string[0] == '-'

    for char in string[::-1]:
        current_integer = char_to_int(char)
        if current_integer != -1:
            num = (decimal * current_integer) + prev
            decimal *= 10
            prev = num

    return num if not negative else num * -1


def int_to_char(integer):
    if integer == 0:
        return '0'
    if integer == 1:
        return '1'
    if integer == 2:
        return '2'
    if integer == 3:
        return '3'
    if integer == 4:
        return '4'
    if integer == 5:
        return '5'
    if integer == 6:
        return '6'
    if integer == 7:
        return '7'
    if integer == 8:
        return '8'
    if integer == 9:
        return '9'
    else:
        return '-1'


def solution2(integer):
    negative = integer < 0

    if negative:
        integer *= -1

    string_number = ''

    while integer > 0:
        right_most = integer % 10
        string_number = int_to_char(right_most) + string_number
        integer //= 10

    return '-'.join(string_number) if negative else string_number


