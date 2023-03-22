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

        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                divTotal += i + num/i
            i += 1
        return int(divTotal) == num
# @lc code=end
