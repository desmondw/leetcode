#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
import math
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [value for row in mat for value in row]
        if r * c != len(flat):
            return mat

        new = []
        for i in range(0, len(flat), c):
            new.append(flat[i:i+c])
        return new
# @lc code=end

