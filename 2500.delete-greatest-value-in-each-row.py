#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        while len(grid[0]) > 0:
            highs = []
            for row in grid:
                top = max(row)
                highs.append(top)
                row.pop(row.index(top))
            total += max(highs)
        return total
# @lc code=end

