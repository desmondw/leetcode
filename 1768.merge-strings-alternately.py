#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ln = min(len(word1),len(word2))
        word3 = ''
        for i in range(ln):
            word3 += word1[i] + word2[i]
        return word3 + word1[ln:] + word2[ln:]
# @lc code=end

