#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        half = len(x)/2
        a = x[:math.floor(half)]
        b = x[math.ceil(half):]
        return a == b[::-1]
# @lc code=end

