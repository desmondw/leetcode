#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
import math
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(len(points)-1):
            total += self.calcDist(points[i],points[i+1])
        return total

    def calcDist(self, a, b) -> int:
        x = abs(a[0]-b[0])
        y = abs(a[1]-b[1])
        return max(x,y)
# @lc code=end

