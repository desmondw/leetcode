#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ns = {}

    def climbStairs(self, n: int) -> int:
        if n < 0: return 0
        elif n <= 1: return 1

        if n not in self.ns:
            self.ns[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.ns[n]
# @lc code=end

