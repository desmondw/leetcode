#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # store k:v as num:freq
        degrees = {}
        maxFreq = 0
        for num in nums:
            if not num in degrees:
                degrees[num] = 0
            degrees[num] += 1
            if degrees[num] > maxFreq:
                maxFreq = degrees[num]

        # get array of nums for all with that freq
        highFreq = []
        for num, freq in degrees.items():
            if freq == maxFreq:
                highFreq.append(num)

        # for each of THOSE nums
        spreads = []
        for num in highFreq:
            # store spread in new array (last index - first index)
            lastIndex = len(nums) - nums[::-1].index(num)
            spread = lastIndex - nums.index(num)
            spreads.append(spread)

        # return min of spread array
        return min(spreads)
# @lc code=end

