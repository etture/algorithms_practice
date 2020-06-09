from __future__ import annotations

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    table = [[0] * (capacity+1) for _ in range(len(weights)+1)]
    for wt_idx, w in enumerate(weights, 1):
        for cap_idx in range(1, capacity+1):
            if w > cap_idx:
                table[wt_idx][cap_idx] = max(
                    table[wt_idx-1][cap_idx],
                    table[wt_idx][cap_idx-1]
                )
            else:
                table[wt_idx][cap_idx] = max(
                    table[wt_idx-1][cap_idx],
                    table[wt_idx][cap_idx-1],
                    table[wt_idx-1][cap_idx-w] + values[wt_idx-1]
                )
    import pprint
    pprint.pprint(table)
    return table[-1][-1]


if __name__ == '__main__':
    w_1 = [1, 2, 3]
    v_1 = [10, 15, 40]
    c_1 = 6

    w_2 = [1, 2, 3]
    v_2 = [60, 100, 120]
    c_2 = 5

    assert knapsack(w_1, v_1, c_1) == 65
    assert knapsack(w_2, v_2, c_2) == 220
