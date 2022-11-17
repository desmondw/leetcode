#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] < 0:
                    total += len(row) - i
                    break
        return total
# @lc code=end

