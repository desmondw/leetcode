#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        result = [] + [None]*len(words)

        for word in words:
            result[int(word[-1])-1] = word[:-1]

        return ' '.join(result)
# @lc code=end

