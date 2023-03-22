#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total ^= num
        return total
# @lc code=end

