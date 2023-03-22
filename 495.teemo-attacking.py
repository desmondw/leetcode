#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        end = -1
        for start in timeSeries:
            total += duration
            if start < end:
                # remove overlapping
                total -= (end - start)
            end = start + duration
        return total

# @lc code=end

