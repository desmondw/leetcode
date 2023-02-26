#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = max(a,b)
        factors = []
        for i in range(1,int(n*math.log(n))+2):
            if a%i + b%i == 0:
                factors.append(i)

        return len(factors)
# @lc code=end

