#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        points = [[0,0]]
        for c in path:
            if   c == 'N': y -= 1
            elif c == 'S': y += 1
            elif c == 'W': x -= 1
            elif c == 'E': x += 1
            else:          raise BaseException(f'uh oh: {c}')
            if [x,y] in points:
                return True
            points.append([x,y])
        return False

# @lc code=end

