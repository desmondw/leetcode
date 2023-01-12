#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
import re
class Solution:
    def countSegments(self, s: str) -> int:
        res = re.split('\s+', s)
        return len([w for w in res if len(w)])
# @lc code=end

