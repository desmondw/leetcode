#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
import functools
class Solution:
    memo = {}

    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        self.memo = {} # WOW -- this needs to be reset or it carries between cases
        subsets = self.getSubsets(nums)
        for sub in subsets:
            sum += self.XORSum(sub)

        return sum

    def getSubsets(self, nums, keys=None):
        if not keys:
            keys = list(range(len(nums)))

        memoKey = str(keys)
        if len(nums) == 0 or memoKey in self.memo:
            return []

        sets = [nums]
        self.memo[memoKey] = True

        for i in range(len(nums)):
            newSet = nums[:]
            newSet.pop(i)
            newKeys = keys[:]
            newKeys.pop(i)

            sets += self.getSubsets(newSet, newKeys)
        return sets

    def XORSum(self, nums):
        return functools.reduce(lambda a,v: a^v, nums)
# @lc code=end

