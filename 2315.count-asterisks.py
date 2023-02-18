#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        outside = True
        for c in s:
            if c == '|':
                outside = not outside
                continue
            if outside and c == '*':
                count+=1
        return count
# @lc code=end

