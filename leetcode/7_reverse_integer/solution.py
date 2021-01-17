class Solution:
    def reverse(self, x: int) -> int:
        MAX = ((2 ** 32) / 2) - 1
        MIN = -((2 ** 32) / 2)
        is_negative = x < 0
        x = abs(x)
        str_x = str(x)
        str_answer = ''
        for char in str_x[::-1]:
            str_answer += char
        int_answer = int(str_answer)
        if is_negative and -int_answer > MIN:
            return -int_answer
        elif int_answer < MAX:
            return int_answer
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(0) == 0
