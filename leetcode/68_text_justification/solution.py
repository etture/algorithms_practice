# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 
# 파이썬 기본 재귀 limit이 1000이라고 함 --> 10^6으로 manual하게 설정
sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
import pprint
pp = pprint.PrettyPrinter()
# ----------------------------------------------------------

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_line_len = 0
        lines = list()
        start_idx = 0
        for idx, word in enumerate(words):
            if cur_line_len + len(word) + 1 <= maxWidth + 1:
                cur_line_len += len(word) + 1
            else:  # exceeds maxWidth
                lines.append(words[start_idx:idx])
                start_idx = idx
                cur_line_len = len(word) + 1
            if idx == len(words) - 1:
                lines.append(words[start_idx:])
        return [self.justify_line(line, maxWidth, last=idx == len(lines) - 1) for idx, line in enumerate(lines)]

    def justify_line(self, words: List[str], maxWidth: int, last: bool = False) -> str:
        # print(f'justify_line -> input: {words}')
        total_word_length = sum(len(word) for word in words)
        spaces = maxWidth - total_word_length

        if last: 
            # print(f'last')
            return ' '.join(words) + ' ' * (spaces - (len(words) - 1))

        if len(words) == 1:
            return words[0] + ' ' * spaces

        slots = len(words) - 1
        spaces_calculated = [0] * slots
        space_idx = 0
        while(spaces > 0):
            # print(f'spaces_calculated: {spaces_calculated}, space_idx: {space_idx}')
            spaces_calculated[space_idx] += 1
            spaces -= 1
            space_idx += 1
            space_idx %= slots
        
        justified_str = list()
        for idx, word in enumerate(words):
            justified_str.append(word)
            if idx < len(words) - 1:
                justified_str.append(' ' * spaces_calculated.pop(0))
        
        return ''.join(justified_str)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [["This", "is", "an", "example", "of", "text", "justification."], 16],
            [
                "This    is    an",
                "example  of text",
                "justification.  "
            ]
        ),
        (
            [["What","must","be","acknowledgment","shall","be"], 16],
            [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ]
        ),
        (
            [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20],
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
            ]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.fullJustify(*input)).run(unordered_output=False)
['What   must   be', 
 'acknowledgment  ', 
 'shall be         ']
['What   must   be', 'acknowledgment  ', 'shall be        ']