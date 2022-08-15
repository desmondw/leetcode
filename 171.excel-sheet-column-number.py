#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = columnTitle[::-1]
        num = 0
        for i,c in enumerate(col):
            val = ord(c) - ord('A') + 1
            num += (26**i) * val
        return num
# @lc code=end

