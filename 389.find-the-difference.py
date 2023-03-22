#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        for c in t:
            if c not in s:
                return c
            s.remove(c)
# @lc code=end

