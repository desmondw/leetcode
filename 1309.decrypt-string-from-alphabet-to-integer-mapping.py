#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s[::-1]
        result = ''

        while len(s):
            if s[0] == '#':
                digit = s[1:3][::-1]
                s = s[3:]
            else:
                digit = s[0]
                s = s[1:]

            result += chr(96 + int(digit))
        return result[::-1]

# @lc code=end

