def n_to_1(n: int) -> int:
    def bottom_up(n: int) -> int:
        if n <= 1:
            return 0
        candidates = list()
        candidates.append(bottom_up(n-1))
        if n % 2 == 0:
            candidates.append(bottom_up(n//2))
        if n % 3 == 0:
            candidates.append(bottom_up(n//3))
        return min(candidates) + 1

    memo = dict()
    def memoization(n: int) -> int:
        if n <= 1:
            return 0
        elif n in memo:
            return memo[n]
        candidates = list()
        candidates.append(memoization(n-1))
        if n % 2 == 0:
            candidates.append(memoization(n//2))
        if n % 3 == 0:
            candidates.append(memoization(n//3))
        memo[n] = min(candidates) + 1
        return memo[n]

    return memoization(n)

if __name__ == '__main__':
    assert n_to_1(1) == 0
    assert n_to_1(4) == 2
    assert n_to_1(7) == 3
    assert n_to_1(10) == 3
    assert n_to_1(11) == 4
