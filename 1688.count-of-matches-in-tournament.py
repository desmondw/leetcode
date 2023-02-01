#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0

        while n > 1:
            matches = n // 2
            n = matches + n % 2
            total += matches

        return total

# @lc code=end

