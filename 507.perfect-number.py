#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False

        divTotal = 1
        i = 2
        end = math.ceil(num/2)
        while i < end:
            if num % i == 0:
                divTotal += i + int(num/i)
                end = math.ceil(num/i)
            i += 1
        return divTotal == num
# @lc code=end

