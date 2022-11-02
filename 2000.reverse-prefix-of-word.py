#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
        i = word.index(ch)
        return word[0:i+1][::-1] + word[i+1:]
# @lc code=end

