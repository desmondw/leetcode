#
# @lc app=leetcode id=2451 lang=python3
#
# [2451] Odd String Difference
#

# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = list(map(lambda v: self.getDiff(v), words))
        solo = min(diffs) if diffs.count(min(diffs)) == 1 else max(diffs)
        return words[diffs.index(solo)]

    def getDiff(self, word):
        res = []
        for j in range(len(word)-1):
            res.append(ord(word[j+1]) - ord(word[j]))
        return str(res)
# @lc code=end

