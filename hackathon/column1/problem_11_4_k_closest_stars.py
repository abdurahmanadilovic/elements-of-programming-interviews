import heapq
import math


class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))


def solution(stars, k):
    heap = []

    for star in stars:
        if len(heap) == k:
            if star.distance() < -heap[0]:
                heapq.heappushpop(heap, -star.distance())
        else:
            heapq.heappush(heap, -star.distance())

    return [-heapq.heappop(heap) for _ in range(len(heap))]

