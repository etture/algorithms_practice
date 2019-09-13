class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        # BRUTE FORCE
        return self.brute_force(s)

        # BETTER METHOD
        # return self.better(s)

    def better(self, s: str):
        pass

    def brute_force(self, s: str):
        palindromes = []
        print(f'str: {s}')
        for start_index in range(0, len(s) - 1):
            for end_index in range(start_index, len(s)):
                seq_to_check = s[start_index:end_index + 1]
                print(f'seq_to_check: {seq_to_check}, is palindrome: {self.check_palindrome(seq_to_check)}')
                if self.check_palindrome(seq_to_check):
                    palindromes.append(seq_to_check)
        print(f'all palindromes: {palindromes}')

        if len(palindromes) > 0:
            print(f'max: {max(palindromes, key=len)}')
            return max(palindromes, key=len)
        else:
            return ''

    def check_palindrome(self, sequence: str) -> bool:
        last_index = len(sequence) - 1
        for index, char in enumerate(sequence):
            if index > len(sequence) // 2:
                break
            if sequence[index] != sequence[last_index - index]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    input1 = 'cbbd'
    input2 = 'ac'
    # input3 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    print(f'input: {input1}, output: {solution.longestPalindrome(input1)}')
    print(f'input: {input2}, output: {solution.longestPalindrome(input2)}')
    # print(f'input: {input3}, output: {solution.longestPalindrome(input3)}')
