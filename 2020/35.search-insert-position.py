#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,n in enumerate(nums):
            if n >= target: return i
        return len(nums)
        
# @lc code=end

