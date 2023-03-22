#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
import math
import re
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return len(re.split(r'[1-9]', str(math.factorial(n)))[-1:][0])
# @lc code=end

