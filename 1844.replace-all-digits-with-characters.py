#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s)//2*2, 2):
            s[i+1] = self.shift(s[i], s[i+1])
        return ''.join(s)

    def shift(self, c, x):
        return chr(ord(c)+int(x))
# @lc code=end

