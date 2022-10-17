#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        if len(coord) == 2: return True

        # sort
        coord.sort(key=lambda p: p[0])
        coord.sort(key=lambda p: p[1])
        print(coord)

        xSame = min(coord, key=lambda p:p[0]) == max(coord, key=lambda p:p[0])
        ySame = min(coord, key=lambda p:p[1]) == max(coord, key=lambda p:p[1])
        if xSame or ySame:
            return True

        # calc line
        xPlus = coord[1][0] - coord[0][0]
        yPlus = coord[1][1] - coord[0][1]
        if yPlus == 0:
            return False
        ratio = xPlus/yPlus

        for i in range(2,len(coord)):
            xDiff = coord[i][0] - coord[i-1][0]
            yDiff = coord[i][1] - coord[i-1][1]
            if not (xDiff == yDiff * ratio):
                return False
        return True
# @lc code=end

