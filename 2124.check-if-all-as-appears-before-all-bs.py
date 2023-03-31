#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        return 'b' not in s or 'a' not in s[s.index('b'):]
# @lc code=end

