#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        col = ''
        while num > 0:
            # chr(65) == 'A'
            ln = int(num % 26) or 26
            col = chr(64+ln) + col
            num = (num-ln)/26

        return col



# @lc code=end

