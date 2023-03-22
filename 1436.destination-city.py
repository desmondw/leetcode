#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, ends = zip(*paths)
        for d in ends:
            if d not in starts:
                return d
        return False
# @lc code=end

