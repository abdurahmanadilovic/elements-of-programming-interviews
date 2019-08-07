def is_valid(path):
    second_last_row = len(path) - 1
    for index in range(second_last_row):
        diff = abs(path[index] - path[-1])
        if diff == 0 or diff == second_last_row - index:
            return False
    return True


def solve(n, row, path, solutions):
    if row == n:
        solutions.append(path[:])
    else:
        for column in range(n):
            path.append(column)
            if is_valid(path):
                solve(n, row + 1, path, solutions)
            path.pop()


def solution(n):
    # return solve(0, 0, n, board, [], [])
    solutions = []
    solve(n, 0, [], solutions)
    return solutions
