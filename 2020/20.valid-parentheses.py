#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l in '({[':
                stack.append(l)
            else:
                if len(stack) == 0: return False
                if l == ')' and stack.pop() != '(': return False
                elif l == ']' and stack.pop() != '[': return False
                elif l == '}' and stack.pop() != '{': return False
        return len(stack) == 0


# @lc code=end

sol = Solution()
print(sol.isValid('{[]}'))
print(sol.isValid('([)]'))