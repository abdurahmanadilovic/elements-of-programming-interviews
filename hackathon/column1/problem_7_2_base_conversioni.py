def letter_to_number(letter):
    if letter == 'A':
        return 10
    if letter == 'B':
        return 11
    if letter == 'C':
        return 12
    if letter == 'D':
        return 13
    if letter == 'E':
        return 14
    if letter == 'F':
        return 15
    else:
        return int(letter)


def int_to_char(integer):
    if integer == 15:
        return 'F'
    if integer == 14:
        return 'E'
    if integer == 13:
        return 'D'
    if integer == 12:
        return 'C'
    if integer == 11:
        return 'B'
    if integer == 10:
        return 'A'
    else:
        return str(integer)


def base_to_decimal(number, base):
    first_index = 1 if number[0] == '-' else 0
    power = len(number) - 1 if first_index == 0 else len(number) - 2

    decimal = 0

    for char in number[first_index:]:
        decimal += letter_to_number(char) * pow(base, power)
        power -= 1

    return decimal


def solution(number, from_base, to_base):
    is_negative = number[0] == '-'

    decimal = base_to_decimal(number, from_base)

    digits = []

    while decimal > 0:
        current_digit = decimal % to_base
        decimal //= to_base
        digits.append(int_to_char(current_digit))

    return '-' + ''.join(reversed(digits)) if is_negative else ''.join(reversed(digits))
