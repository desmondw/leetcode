#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = chr(ord('a') + i)


        for i in range(len(words)):
            word = ''
            for c in words[i]:
                word += orderMap[c]
            words[i] = word

        return words == sorted(words)
# @lc code=end

