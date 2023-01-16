#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # tile = grid[y][x]
                if grid[y][x] == 0:
                    continue

                if x == 0 or grid[y][x-1] == 0:
                    count += 1
                if y == 0 or grid[y-1][x] == 0:
                    count += 1
                if x == len(grid[0])-1 or grid[y][x+1] == 0:
                    count += 1
                if y == len(grid)-1 or grid[y+1][x] == 0:
                    count += 1
        return count

# @lc code=end

