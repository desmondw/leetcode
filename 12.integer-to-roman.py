#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
from math import floor
class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            '': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        order = ['M','D','C','L','X','V','I']
        subs = {
            'I': '',
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X',
            'D': 'C',
            'M': 'C',
        }
        roman = ''

        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        for c in order:
            # if
            val = values[c]
            sub = values[subs[c]]

            quotient = floor(num/val)
            subQuotient = floor((num+sub)/val)
            roman += c * quotient
            num -= val * quotient
            if quotient < subQuotient:
                roman += subs[c] + c
                num -= val - sub
            # print('num',num, 'quotient',quotient, 'val',val)
            # print(roman)

        return roman

# @lc code=end

