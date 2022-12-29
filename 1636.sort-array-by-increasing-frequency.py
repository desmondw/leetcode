#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1

        cohorts = {}
        for (num, freq) in freqMap.items():
            if freq not in cohorts:
                cohorts[freq] = []
            cohorts[freq].append(num)

        # sort by num array, then by freq
        cohorts = list(cohorts.items())
        cohorts.sort()

        result = []
        for pair in cohorts:
            pair[1].sort()
            for n in pair[1][::-1]:
                result += [n] * pair[0]

        return result

# @lc code=end

