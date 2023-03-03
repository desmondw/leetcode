#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        top = 0
        cur = 0
        for x in gain:
            cur += x
            if cur > top:
                top = cur
        return top
# @lc code=end

