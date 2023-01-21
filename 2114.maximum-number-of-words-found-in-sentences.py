#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        top = 0
        for s in sentences:
            top = max(top, len(s.split(' ')))
        return top
# @lc code=end

