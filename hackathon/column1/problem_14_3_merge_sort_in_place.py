def solution(a, b):
    # try to write largest at the end
    latest_a_index = 0
    for index, item in enumerate(a):
        if item == ' ':
            latest_a_index = index - 1
            break

    i, j = latest_a_index, len(b) - 1
    index_to_write = i + len(b)

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[index_to_write] = a[i]
            index_to_write -= 1
            i -= 1
        else:
            a[index_to_write] = b[j]
            index_to_write -= 1
            j -= 1

    while j >= 0:
        a[index_to_write] = b[j]
        j -= 1
        index_to_write -= 1

    return a
