#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            i1 = s.find(part)
            i2 = i1 + len(part)
            s = s[:i1] + s[i2:]
        return s
# @lc code=end

