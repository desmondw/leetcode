#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1))+list(set(nums2))+list(set(nums3))
        filt = [num for i,num in enumerate(nums) if num in nums[0:i]+nums[i+1:]]
        return list(set(filt))
# @lc code=end

