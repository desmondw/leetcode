#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        length = max(len(start),len(goal))
        start = start.zfill(length)
        goal = goal.zfill(length)
        return len([i for (i,x) in enumerate(start) if goal[i] != x])
# @lc code=end

