#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = list(set(nums))
        dupes = nums[:]
        while len(unique):
            dupes.remove(unique.pop())
        return sum([v for v in nums if v not in dupes])
# @lc code=end

