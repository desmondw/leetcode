#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1 if len(s) else 0
        line = 0
        for c in s:
            cw = widths[ord(c)-97]
            if line + cw > 100:
                lines += 1
                line = 0
            line += cw
        return [lines, line]
# @lc code=end

