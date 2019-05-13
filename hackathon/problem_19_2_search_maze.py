from itertools import product


def dps(x, y, maze, visited):
    if y == len(maze) or x == len(maze[y]):
        return -1
    if visited[y][x]:
        return -1
    if maze[y][x] == 'w':
        return -1
    if maze[y][x] == 'e':
        return 1

    visited[y][x] = True

    for x_move, y_move in list(product([-1, 0, 1], [-1, 0, 1])):
        if dps(max(x + x_move, 0), max(y + y_move, 0), maze, visited) == 1:
            return True
    return False


def dps_no_recursion(maze, visited):
    to_process = [(0, 0)]

    while len(to_process) > 0:
        current = to_process.pop()

        visited[current[1]][current[0]] = True

        if maze[current[1]][current[0]] == 'e':
            return True

        for x_move, y_move in list(product([-1, 0, 1], [-1, 0, 1])):
            new_x, new_y = max(current[0] + x_move, 0), max(current[1] + y_move, 0)

            if new_y == len(maze) or new_x == len(maze[new_y]):
                continue
            if visited[new_y][new_x] or maze[new_y][new_x] == 'w':
                continue

            to_process.append((new_x, new_y))

    return False


def solution2(maze):
    if len(maze) == 0:
        return False

    visited = []
    for row in maze:
        visited.append([False] * len(row))

    return dps_no_recursion(maze, visited)


def solution(maze):
    """
    maze is 2d array, DPS till I find a solution?
    """
    if len(maze) == 0:
        return False

    visited = []
    for row in maze:
        visited.append([False] * len(row))

    return dps(0, 0, maze, visited)
