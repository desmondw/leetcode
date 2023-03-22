#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        result = []
        for word in words:
            word = word.lower()
            if len(word) > 2:
                word = word[0].upper() + word[1:]
            result.append(word)
        return ' '.join(result)
# @lc code=end

