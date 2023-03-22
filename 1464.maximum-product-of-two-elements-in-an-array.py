#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = (nums[0]-1)*(nums[1]-1)
        r = (nums[len(nums)-2]-1)*(nums[len(nums)-1]-1)
        return max(l,r)
# @lc code=end

