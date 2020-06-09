def lcs(seq_1: str, seq_2: str) -> int:
    table = [[0] * (len(seq_1)+1) for _ in range(len(seq_2)+1)]
    seq_1_padded, seq_2_padded = f' {seq_1}', f' {seq_2}'
    for s1_idx in range(1, len(seq_1)+1):
        for s2_idx in range(1, len(seq_2)+1):
            # print(f's1_idx: {s1_idx}, s2_idx: {s2_idx}, table:')
            from pprint import pprint
            # pprint(table)
            if seq_1_padded[s1_idx] == seq_2_padded[s2_idx]:
                table[s2_idx][s1_idx] = table[s2_idx-1][s1_idx-1] + 1
            else:
                table[s2_idx][s1_idx] = max(
                    table[s2_idx-1][s1_idx],
                    table[s2_idx][s1_idx-1]
                )
    return table[-1][-1]

if __name__ == '__main__':
    pair_1 = ('hamburger', 'amber')
    pair_2 = ('abcdefg', 'aceg')

    assert lcs(*pair_1) == 5
    assert lcs(*pair_2) == 4
    print(lcs(*pair_1))
