#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
import math
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        items = sorted(nums)[::-1]

        for i in range(l1:=len(items)):
            a = items[i]
            if i < l1-2 and a >= items[i+1] + items[i+2]: continue
            bRange = items[i+1:]
            for j in range(l2:=len(bRange)):
                b = bRange[j]
                cRange = items[i+1:][j+1:]
                for k in range(l3:=len(cRange)):
                    c = cRange[k]
                    if a < (b + c):
                        return a + b + c
        return 0

# @lc code=end

