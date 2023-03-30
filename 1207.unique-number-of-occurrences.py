#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = {}
        for n in arr:
            if n not in freqMap:
                freqMap[n] = 0
            freqMap[n] += 1
        res = list(freqMap.values())
        return sorted(res) == sorted(list(set(res)))
# @lc code=end

