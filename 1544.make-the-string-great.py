#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        while i < len(s):
            if abs(ord(s[i-1]) - ord(s[i])) == 32:
                s = s[:i-1] + s[i+1:]
                i = 1
            else:
                i += 1
        return s
# @lc code=end

