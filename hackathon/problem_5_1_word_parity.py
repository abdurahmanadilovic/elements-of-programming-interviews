def solution2(n):
    """
    efficiently calculate parity of a large 64 bit word
    """
    ones = 0
    while n > 0:
        if n & 1:
            ones += 1
        n = n >> 1

    return 0 if ones % 2 == 0 else 1


def parity(n):
    current_parity = 0

    while n > 0:
        current_parity ^= n & 1
        n = n >> 1

    return current_parity


def solution4(n):
    cache = {}
    """
    fix this by processing more bits at once, use 16 bits and compute parity
    of 4 16 bit sub words of the original 64 bit word!
    """
    mask = (1 << 16) - 1
    current_parity = 0

    while n > 0:
        bits1 = n & mask
        bits2 = n >> 16 & mask
        bits3 = n >> 32 & mask
        bits4 = n >> 48 & mask
        cache[bits1] = cache.get(bits1, parity(bits1))
        cache[bits2] = cache.get(bits2, parity(bits2))
        cache[bits3] = cache.get(bits3, parity(bits3))
        cache[bits4] = cache.get(bits4, parity(bits4))
        current_parity ^= cache[bits1]
        current_parity ^= cache[bits2]
        current_parity ^= cache[bits3]
        current_parity ^= cache[bits4]
        n >>= 64

    return current_parity


def solution3(n):
    current_parity = 0
    while n > 0:
        n &= n - 1
        current_parity ^= 1
    return current_parity


def solution(n):
    n ^= n >> 32
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n & 1


