class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        split_tokens = re.split('\s+', s.strip())
        return ' '.join(split_tokens[::-1])


if __name__ == '__main__':
    sltn = Solution()
    assert sltn.reverseWords("the sky is blue") == "blue is sky the"
    assert sltn.reverseWords("a good   example") == "example good a"
    assert sltn.reverseWords("  hello world  ") == "world hello"
    assert sltn.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
