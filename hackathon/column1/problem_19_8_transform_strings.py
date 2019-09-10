from collections import deque, defaultdict


def solution(dict_of_words, s, t):
    graph = defaultdict(dict)

    for word in dict_of_words:
        if word != s and word != t:
            cost = calculate_cost(word, s)
            if cost == 1:
                graph[s][word] = 1

    queue = deque(graph[s].keys())
    visited = defaultdict(bool)

    while len(queue) > 0:
        current = queue.popleft()
        if visited[current]:
            continue

        visited[current] = True

        for word in dict_of_words:
            if word != current:
                cost = calculate_cost(word, current)
                if cost == 1:
                    graph[current][word] = cost

        next_nodes = graph[current].keys()
        if next_nodes:
            queue.extend(next_nodes)

    path_size = find_shortest_path(graph, s, t)
    return path_size if path_size > 0 else -1


def calculate_cost(a, b):
    cost = 0

    for index in range(len(a)):
        if a[index] != b[index]:
            cost += 1

    return cost


def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return count_elements(dist[end])


def count_elements(list):
    count = 0
    for item in list:
        if type(item) != type([]):
            count += 1
        else:
            count += count_elements(item)

    return count
