#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = '-' if num < 0 else ''
        num = abs(num)
        result = ''

        # 7^9 max places
        for i in range(9,1,-1):
            count = 0
            oneIndexValue = 7**(i-1)
            while num - oneIndexValue >= 0:
                num -= oneIndexValue
                count += 1
            result += str(count)
        result += str(num)

        result = result.lstrip('0')
        if not result:
            result = '0'
        return sign + result

# @lc code=end

