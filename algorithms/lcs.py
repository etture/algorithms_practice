"""Longest common subsequence"""

def lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    L = [[None] * (n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif seq1[i-1] == seq2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[m][n]

if __name__ == '__main__':
    print(lcs('ABCDEFG', 'ACEFSJLKJE'))