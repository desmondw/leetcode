#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        total = 0
        for i,n in enumerate(sorted(heights)):
            if heights[i] != n:
                total += 1

        return total
# @lc code=end

