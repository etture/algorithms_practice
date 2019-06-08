class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        if s == '':
            return 0
        else:
            for char in s:
                if len(substrings) == 0:
                    substrings.append(char)
                else:
                    if char not in substrings[-1]:
                        substrings.append(substrings[-1] + char)
                    else:
                        char_index = substrings[-1].find(char)
                        substrings.append(substrings[-1][char_index+1:] + char)
            print(f'substrings: {substrings}')
            return len(max(substrings, key=len))


if __name__ == '__main__':
    solution = Solution()
    input1 = 'abcabcbb'
    input2 = 'dvdf'
    input3 = 'pwwkew'
    print(solution.lengthOfLongestSubstring(input1))
    print(solution.lengthOfLongestSubstring(input2))
    print(solution.lengthOfLongestSubstring(input3))
