#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            tally = 0
            for point in points:
                dx = point[0]-query[0]
                dy = point[1]-query[1]
                dist = math.sqrt(dx**2 + dy**2)
                radius = query[2]
                if dist <= radius:
                    tally += 1
            answer.append(tally)

        return answer


# @lc code=end

