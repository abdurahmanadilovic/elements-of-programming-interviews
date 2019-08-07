def print_top(array, row_padding, column_padding_left, column_padding_right):
    return [cell for cell in array[row_padding][column_padding_left:column_padding_right]]


def print_right_side(array, row_padding_top, row_padding_bottom, column_padding_right):
    return [row[column_padding_right] for row in array[row_padding_top+1: row_padding_bottom-1]]


def print_left_side(array, row_padding_top, row_padding_bottom, column_padding_left):
    return [row[column_padding_left] for row in reversed(array[row_padding_top+1: row_padding_bottom-1])]


def print_bottom(array, row_padding_bottom, column_padding_left, column_padding_right):
    return [column for column in reversed(array[row_padding_bottom][column_padding_left:column_padding_right])]


def iterate(array, row_padding_top, row_padding_bottom, column_padding_left, column_padding_right):
    if row_padding_top >= row_padding_bottom or column_padding_left >= column_padding_right:
        return []
    else:
        return print_top(array, row_padding_top, column_padding_left, column_padding_right)\
               + print_right_side(array, row_padding_top, row_padding_bottom, column_padding_right-1)\
               + print_bottom(array, row_padding_bottom - 1, column_padding_left, column_padding_right)\
               + print_left_side(array, row_padding_top, row_padding_bottom, column_padding_left)\
               + iterate(array, row_padding_top + 1, row_padding_bottom - 1, column_padding_left + 1,
                         column_padding_right - 1)


def solution(array):
    result = iterate(array, 0, len(array), 0, len(array[0]))
    if result[-1] == result[-2]:
        result.pop()
    return result
