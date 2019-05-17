def solution(s):
    write_index = 0
    a_count = 0

    for char in s:
        if char != 'b':
            s[write_index] = char
            write_index += 1
        if char == 'a':
            a_count += 1

    s = s[:write_index] + ['' for _ in range(a_count)]

    write_index = len(s) - 1

    for char in s[::-1]:
        if not char:
            continue

        if char == 'a':
            s[write_index] = 'd'
            write_index -= 1
            s[write_index] = 'd'
            write_index -= 1
        else:
            s[write_index] = char
            write_index -= 1

    return s

