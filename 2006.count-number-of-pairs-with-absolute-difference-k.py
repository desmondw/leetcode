#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)-1):
            for j in range(len(nums)-i):
                if abs(nums[i] - nums[i+j]) == k:
                    total += 1

        return total
# @lc code=end

