#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
import functools
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = functools.reduce(lambda a,v:a*v, nums, 1)
        return 0 if not product else int(product/abs(product))
# @lc code=end

