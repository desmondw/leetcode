#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        lists = []
        for i, num in enumerate(nums):
            psuedoSplice = nums[:i] + nums[i+1:]
            sublists = self.permute(psuedoSplice)

            for sublist in sublists:
                lists.append([num] + sublist)

        return lists
# @lc code=end

