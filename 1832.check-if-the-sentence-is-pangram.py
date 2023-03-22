#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = 0
        for c in string.ascii_lowercase:
            if c in sentence:
                count += 1
        return count == 26
# @lc code=end

