#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True

        for i in range(len(nums)-1):
            if   nums[i] < nums[i+1]: dec = False
            elif nums[i] > nums[i+1]: inc = False
            if not inc and not dec:
                break

        return inc or dec

# @lc code=end

