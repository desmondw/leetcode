#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
import functools
class Solution:
    def isHappy(self, n: int) -> bool:
        prev = {n:True}
        while n != 1:
            n = functools.reduce(lambda a,v: a+int(v)**2,list(str(n)),0)
            if n in prev: return False
            prev[n] = True
        return True
# @lc code=end

