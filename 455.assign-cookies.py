#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        for greed in g:
            res = True
            while len(s) and (res:=(s.pop(0) < greed)):
                pass
            if not res:
                count += 1
            if not len(s):
                return count

        return count
# @lc code=end

