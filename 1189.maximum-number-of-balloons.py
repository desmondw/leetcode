#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = ['b','a','l','o','n']
        counts = {}
        for c in letters:
            counts[c] = len([x for x in text if x == c])
        counts['l'] = int(counts['l']/2)
        counts['o'] = int(counts['o']/2)
        return min(counts['b'], counts['a'], counts['l'], counts['o'], counts['n'])

# @lc code=end

