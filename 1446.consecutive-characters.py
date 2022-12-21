#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        best = 0
        text = s[0]
        for c in s[1:]:
            if c == text[0]:
                text += c
            else:
                best = max(best, len(text))
                text = c
        best = max(best, len(text))
        return best

# @lc code=end

