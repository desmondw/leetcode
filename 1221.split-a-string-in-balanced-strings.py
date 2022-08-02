#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sub = ''
        count = 0

        for c in s:
            if self.isBalanced(sub := sub + c):
                count += 1
                sub = ''

        return count

    def isBalanced(self, str: str) -> bool:
        return str.count('R') == str.count('L')



# @lc code=end

