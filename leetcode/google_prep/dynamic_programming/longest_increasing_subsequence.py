from __future__ import annotations

def lis(sequence: List[int]) -> int:
    memo = [1] * len(sequence)
    for i in range(len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                memo[i] = max(memo[i], memo[j]+1)
    # print(memo)
    return max(memo)

if __name__ == '__main__':
    seq_1 = [10, 22, 9, 33, 21, 50, 41, 60]
    seq_2 = [3, 10, 2, 11]
    seq_3 = [2, 1, 3, 4, 5, 6, 4, 3, 5, 1, 10]
    
    assert lis(seq_1) == 5
    assert lis(seq_2) == 3
    assert lis(seq_3) == 6
