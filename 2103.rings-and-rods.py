#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for x in range(10)]
        for i in range(0,len(rings),2):
            color = rings[i]
            rod = int(rings[i+1])
            rods[rod].add(color)
        return len([x for x in rods if len(list(x)) == 3])
# @lc code=end

