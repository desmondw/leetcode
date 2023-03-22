#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        arr = sorted(filter(lambda v: v in '0123456789', set(s)))
        # print(arr)
        return -1 if len(arr) < 2 else int(arr[-2])
# @lc code=end

