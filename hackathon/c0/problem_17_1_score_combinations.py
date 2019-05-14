def solution(score):
    # solutions = {}
    # solve(0, score, [], solutions)
    # return len(solutions.keys())
    return solve2(score)


def solve(current_score, target_score, path, solutions):
    if current_score > target_score:
        return 0
    elif current_score == target_score:
        path_sorted = str(sorted(path))
        if path_sorted not in solutions:
            solutions[path_sorted] = 1
            print(path)
        return 1
    else:
        combinations = solve(current_score + 7, target_score, path[:] + [7], solutions)
        combinations += solve(current_score + 3, target_score, path[:] + [3], solutions)
        combinations += solve(current_score + 2, target_score, path[:] + [2], solutions)
        return combinations


def solve2(score):
    solutions = [0] * (score + 1)
    solutions[0] = 1
    for single_score in [7, 3, 2]:
        for index in range(single_score, score + 1):
            solutions[index] += solutions[index - single_score]

    return solutions[score]

