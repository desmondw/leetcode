#
# @lc app=leetcode id=1037 lang=python3
#
# [1037] Valid Boomerang
#

# @lc code=start
class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        # SO STUPID. I hate math problems. Hours wasted.
        x1,y1 = p[0]
        x2,y2 = p[1]
        x3,y3 = p[2]
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
# @lc code=end

