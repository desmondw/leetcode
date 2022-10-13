#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processString(s) == self.processString(t)

    def processString(self, str):
        result = ''
        count = 0
        for c in str[::-1]:
            if c == "#":
                count+=1
            elif count > 0:
                count-=1
            else:
                result += c
        return result[::-1]
# @lc code=end

