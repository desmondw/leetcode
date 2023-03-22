#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        top = 0
        cur = 0
        for c in s:
            if c == '(':
                cur += 1
                if cur > top:
                    top = cur
            elif c == ')':
                cur -= 1
        return top
# @lc code=end

