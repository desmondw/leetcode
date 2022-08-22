#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        cur = upper//2

        while target != nums[cur]:
            print('l',lower,'u',upper,'c',cur)
            if target < nums[cur]: upper = cur
            else: lower = cur
            cur = lower + (upper-lower)//2
            if (upper-lower <= 1): break

        if target == nums[cur]: return cur
        elif target <= nums[lower]: return lower
        elif target <= nums[upper]: return upper
        elif target > nums[upper]: return upper+1
        return None
# @lc code=end

