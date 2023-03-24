#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        top = -1
        for i in range(len(s)):
            print(i)
            for j in range(len(s)-1, i, -1):
                print(i, j)
                if s[i] == s[j]:
                    diff = j - i - 1
                    if diff > top:
                        top = diff
                    break
        return top
# @lc code=end

