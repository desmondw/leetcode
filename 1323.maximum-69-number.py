#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        if (i:=num.find('6')) >= 0:
            num = num[:i] + '9' + num[i+1:]
        return int(num)
# @lc code=end

