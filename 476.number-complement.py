#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
import re
class Solution:
    def findComplement(self, num: int) -> int:
        return int('0b'+bin(num)[2:].replace('1','2').replace('0','1').replace('2','0'), 2)
# @lc code=end
