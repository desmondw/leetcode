#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a = {'x1':rec1[0],'y1':rec1[1],'x2':rec1[2],'y2':rec1[3]}
        b = {'x1':rec2[0],'y1':rec2[1],'x2':rec2[2],'y2':rec2[3]}
        return (a['x1'] < b['x2'] and a['x2'] > b['x1']) and (a['y1'] < b['y2'] and a['y2'] > b['y1'])
# @lc code=end

