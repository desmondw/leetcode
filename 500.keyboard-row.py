#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        validWords = []
        for word in words:
            testWord = ''.join(list(set(word.lower())))
            if self.checkValid(testWord):
                validWords.append(word)
        return validWords

    def checkValid(self, word):
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]

        for row in rows:
            valid = True
            for c in word:
                if c not in row:
                    valid = False
                    break
            if valid: return True
        return False

# @lc code=end

