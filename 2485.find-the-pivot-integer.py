#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = sum(range(1,n+1))
        for x in range(1,n+1):
            left += x
            right -= x
            if left == right + x:
                return x
            elif left > right:
                return -1
        return -1
# @lc code=end

