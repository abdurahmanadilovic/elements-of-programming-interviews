def solution(a, b, c):
    return move2(len(a), a, b, c, 0)


def move(position, current, target, intermediate, moves):
    if position == len(current) - 1:
        if len(target) == 0 or target[-1] > current[position]:
            item = current.pop()
            target.append(item)
            return moves + 1
        else:
            item_to_move = None
            while len(target) > 0 and target[-1] < current[position]:
                item_to_move = target[-1]
                moves += move(len(target) - 1, target, intermediate, current, 0)
            item = current.pop()
            target.append(item)

            index_of_moved = -1
            for index in range(len(intermediate)):
                if intermediate[index] == item_to_move:
                    index_of_moved = index
            if index_of_moved != -1:
                moves += move(index_of_moved, intermediate, target, current, 0)

            return moves + 1
    else:
        return move(position + 1, current, target, intermediate, 0) + move(position, current, target, intermediate, 0)


def move2(num_of_rings, current, target, intermediate, count):
    if num_of_rings > 0:
        count += move2(num_of_rings - 1, current, intermediate, target, 0)

        count += 1
        target.append(current.pop())

        return count + move2(num_of_rings - 1, intermediate, target, current, 0)
    return count
