def solution(array1, array2):
    if len(array2) == 0 or len(array1) == 0:
        return []
    i = 0
    j = 0
    res = []
    while i < len(array1) and j < len(array2):
        while array2[j] < array1[i]:
            j += 1
        else:
            if array2[j] == array1[i]:
                res.append(array1[i])
                i += 1
                while array1[i] == array2[j]:
                    j += 1
            else:
                i += 1
    return res
