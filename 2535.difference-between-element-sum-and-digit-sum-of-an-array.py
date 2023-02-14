#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nums2 = [int(y) for y in ''.join([str(x) for x in nums])]
        return abs(sum(nums)-sum(nums2))
# @lc code=end

