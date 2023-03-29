#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([x for x in words if pref in x and x.index(pref) == 0])
# @lc code=end

