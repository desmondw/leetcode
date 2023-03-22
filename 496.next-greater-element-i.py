#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n1 in nums1:
            v = -1
            for j in range(nums2.index(n1)+1, len(nums2)):
                if n1 < nums2[j]:
                    v = nums2[j]
                    break
            result.append(v)
        return result
# @lc code=end

