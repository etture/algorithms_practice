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
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # objective is to lump largest sum sub-array into single group
        jobs_len = len(jobDifficulty)
        dp = [[-1] * jobs_len for day in range(d)]
        for day_idx in range(d):
            for job_idx in range(day_idx, jobs_len):
                if day_idx == job_idx:
                    if day_idx > 0:
                        dp[day_idx][job_idx] = jobDifficulty[job_idx] + dp[day_idx-1][job_idx-1]
                    else:  # just one day
                        dp[day_idx][job_idx] = jobDifficulty[job_idx]
                elif day_idx == 0:
                    if jobDifficulty[job_idx] >= dp[day_idx][job_idx-1]:
                        dp[day_idx][job_idx] = jobDifficulty[job_idx]
                    else:
                        dp[day_idx][job_idx] = dp[day_idx][job_idx-1]
                else:
                    if jobDifficulty[job_idx] <= jobDifficulty[job_idx-1]:
                        dp[day_idx][job_idx] = min(dp[day_idx][job_idx-1], jobDifficulty[job_idx] + dp[day_idx-1][job_idx-1])
                    else:
                        min_prev = 99999999
                        faced_bigger = False
                        tmp_idx = job_idx
                        while tmp_idx - 1 >= day_idx - 1:
                            tmp_idx -= 1
                            if jobDifficulty[tmp_idx] > jobDifficulty[job_idx]:
                                # min_prev = dp[day_idx-1][tmp_idx]
                                min_prev = min(dp[day_idx-1][tmp_idx], min_prev)
                                faced_bigger = True
                                break
                            min_prev = dp[day_idx-1][tmp_idx]
                            # min_prev = min(dp[day_idx-1][tmp_idx], min_prev)
                            # tmp_idx -= 1
                        if faced_bigger:
                            prev_carry = dp[day_idx][tmp_idx] if dp[day_idx][tmp_idx] >= 0 else dp[day_idx][job_idx-1]
                            dp[day_idx][job_idx] = min(prev_carry, jobDifficulty[job_idx] + min_prev)
                            # dp[day_idx][job_idx] = min(dp[day_idx][tmp_idx], jobDifficulty[job_idx] + min_prev)
                            # dp[day_idx][job_idx] = jobDifficulty[job_idx] + min_prev
                        else:
                            dp[day_idx][job_idx] = min_prev + jobDifficulty[job_idx]
                # pp.pprint(dp)
                print('==========================================================')
                row_str = list()
                for num in jobDifficulty:
                    num_str = [' '] + list(str(num))
                    if len(num_str) < 5:
                        for _ in range(5-len(num_str)):
                            num_str.append(' ')
                    row_str.append(''.join(num_str))
                print(','.join(row_str))
                # print(jobDifficulty)
                print('==========================================================')
                for row in dp:
                    row_str = list()
                    for num in row:
                        num_str = [' '] + list(str(num))
                        if len(num_str) < 5:
                            for _ in range(5-len(num_str)):
                                num_str.append(' ')
                        row_str.append(''.join(num_str))
                    print(','.join(row_str))
                print()
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        # ([[6,5,4,3,2,1], 2], 7),
        # ([[6,5,4,3,2,1], 3], 9),
        # ([[9,9,9], 4], -1),
        # ([[9,9,9], 3], 27),
        # ([[9,9,9], 2], 18),
        # ([[1,1,1], 3], 3),
        # ([[7,1,7,1,7,1], 3], 15),
        # ([[11,111,22,222,33,333,44,444], 6], 843),
        # ([[11,111,22,222,33,333,44,444, 5, 2, 1], 9], 851),
        # ([[10, 35, 72, 100, 49, 25, 8], 5], 178),
        # ([[10, 35, 72, 100, 49, 70, 8], 5], 223),
        # ([[186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360], 4], 1803),
        ([[380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315], 10], 3807)
    ]

    Tester.factory(test_cases, func=lambda input: sol.minDifficulty(*input)).run(unordered_output=False)
