#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matrix = []
        for i in range(1,len(grid)-1):
            matrixRow = []
            for j in range(1,len(grid[0])-1):
                a = grid[i-1][j-1:j+2]
                b = grid[i][j-1:j+2]
                c = grid[i+1][j-1:j+2]
                matrixRow.append(max(a+b+c))
            matrix.append(matrixRow)
        return matrix
# @lc code=end

