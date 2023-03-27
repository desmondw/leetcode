#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [0]

        ls = 0
        rs = sum(nums[1:])
        sums = [abs(ls - rs)]
        for i in range(1, len(nums)-1):
            ls += nums[i-1]
            rs -= nums[i]
            sums.append(abs(ls-rs))
        sums.append(abs(sum(nums[:-1]) - 0))

        return sums
# @lc code=end

