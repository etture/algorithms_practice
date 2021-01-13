from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = dict()
        row = 0
        ascending = True
        for char in s:
            if row not in zigzag:
                zigzag[row] = list()
            zigzag[row].append(char)
            if ascending:
                row += 1
                if row == numRows-1:
                    ascending = False
            else:
                row -= 1
                if row == 0:
                    ascending = True
        answer = ''
        for row in range(numRows):
            if row not in zigzag:
                continue
            answer += ''.join(zigzag[row])
        print(answer)
        return answer


if __name__ == '__main__':
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    assert sol.convert("A", 2) == "A"
    assert sol.convert("AB", 1) == "AB"
