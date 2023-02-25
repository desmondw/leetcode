#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        total = 0
        for i in range(l):
            total += mat[i][i]
            if (i2 := l-1-i) != i:
                total += mat[i][i2]
        return total
# @lc code=end