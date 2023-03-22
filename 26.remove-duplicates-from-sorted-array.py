#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                del nums[i+1]
            i+=1
# @lc code=end

