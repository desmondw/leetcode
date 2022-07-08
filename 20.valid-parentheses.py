#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c not in map.keys():
                stack.append(c)
            else:
                if not len(stack) or stack.pop() != map[c]:
                    return False
        return not len(stack)
# @lc code=end

