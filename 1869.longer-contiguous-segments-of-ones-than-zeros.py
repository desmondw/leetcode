#
# @lc app=leetcode id=1869 lang=python3
#
# [1869] Longer Contiguous Segments of Ones than Zeros
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s += 'x'
        long0 = 0
        long1 = 0
        cur = ''
        for c in s:
            if not cur or cur[0] == c:
                cur += c
            else:
                l = len(cur)
                if cur[0] == '0' and l > long0:
                    long0 = l
                elif cur[0] == '1' and l > long1:
                    long1 = l
                cur = c
        return long1 > long0
# @lc code=end

