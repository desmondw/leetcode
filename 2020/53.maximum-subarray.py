#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float('-inf')
        for i in range(len(nums)):
            subtotal = 0
            for j in range(i, len(nums)):
                subtotal += nums[j]
                if (subtotal > max): max = subtotal
        return max

# @lc code=end

