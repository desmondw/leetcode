#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freqHash = {}
        for c in words[0]:
            if c not in freqHash: freqHash[c] = 0
            freqHash[c] += 1
        for word in words[1:]:
            for c, num in list(freqHash.items()):
                freqHash[c] = min(word.count(c), num)
                if freqHash[c] == 0: freqHash.pop(c)

        result = []
        for k,n in freqHash.items():
            for i in range(0,n):
                result.append(k)
        return result
# @lc code=end

