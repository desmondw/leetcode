#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            idx = t.find(c)
            if idx < 0:
                return False
            t = t[idx+1:]
        return True
# @lc code=end

