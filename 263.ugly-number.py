#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 1:
            if   not n%2: n/=2
            elif not n%3: n/=3
            elif not n%5: n/=5
            else: return n==0
        return n > 0

# @lc code=end

