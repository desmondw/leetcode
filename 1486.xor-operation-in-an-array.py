#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n < 2: return start
        x = start
        for i in range(1, n):
            x = x ^ start+2*i

        return x
# @lc code=end

