#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        low1 = nums.pop(nums.index(min(nums)))
        low2 = min(nums)
        high1 = nums.pop(nums.index(max(nums)))
        high2 = max(nums)
        return abs(low1 * low2 - high1 * high2)
# @lc code=end

