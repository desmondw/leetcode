#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        res = ''
        for c in s:
            if c == ')':
                depth -= 1
            res += c if depth > 0 else ''
            if c == '(':
                depth += 1
        return res

# @lc code=end

