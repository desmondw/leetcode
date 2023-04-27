#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = int(n * (1 + n) /2)

        hashd = {}
        runningSum = 0
        dupe = None
        for i in range(n):
            runningSum += nums[i]
            if nums[i] not in hashd:
                hashd[nums[i]] = True
            else:
                dupe = nums[i]
                runningSum += sum(nums[i+1:])
                break

        return [dupe, total-(runningSum-dupe)]
# @lc code=end

