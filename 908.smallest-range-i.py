#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = nums[0] + k
        high = nums[-1] - k

        return max(0, high-low)
# @lc code=end

