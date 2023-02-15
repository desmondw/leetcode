#
# @lc app=leetcode id=2520 lang=python3
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        return sum([1 for x in list(str(num)) if num % int(x) == 0])
# @lc code=end

