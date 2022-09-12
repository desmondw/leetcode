#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-z\s]', ' ', paragraph.lower())
        paragraph = re.sub(r'\s+', ' ', paragraph)
        words = paragraph.split(' ')

        freqHash = {'': 0}
        top = ''
        for word in words:
            if word not in banned:
                if word not in freqHash:
                    freqHash[word] = 0
                freqHash[word] += 1

                if freqHash[word] > freqHash[top]:
                    top = word
        return top



# @lc code=end

