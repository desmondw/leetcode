#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,n):
            nums1.pop()
        for i, n1 in enumerate(nums1):
            if nums2 and nums2[0] <= n1: nums1.insert(i, nums2.pop(0))

        # remainders on nums2
        nums1.extend(nums2)
        
        return nums1
        
# @lc code=end

