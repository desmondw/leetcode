#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        (a,b) = s.split(':')
        colRange = (ord(a[0]), ord(b[0])+1)
        rowRange = (int(a[1]), int(b[1])+1)
        res = []

        for c in range(*colRange):
            res += [f'{chr(c)}{x}' for x in range(*rowRange)]

        return res
# @lc code=end

