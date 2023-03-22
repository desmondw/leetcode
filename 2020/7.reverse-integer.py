#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        val = int(str(abs(x))[::-1]) * sign
        if (val < -2**31 or val > 2**31): return 0
        return val
        
# @lc code=end

