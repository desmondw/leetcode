#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        longest = 0
        s = bin(n)[2:].strip('0')
        if len(s) < 2:
            return 0

        cur = 1
        for c in s:
            if c == '0':
                cur += 1
            else:
                if cur > longest:
                    longest = cur
                cur = 1
        return longest

# @lc code=end

