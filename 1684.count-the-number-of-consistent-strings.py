#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words = [list(set(x)) for x in words]
        resp = [all(v in allowed for v in  word) for word in words]
        return sum(resp)
# @lc code=end

