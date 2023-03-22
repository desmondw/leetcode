#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d = [int(x) for x in str(n)]
        return math.prod(d) - sum(d)
# @lc code=end

