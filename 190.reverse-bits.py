#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[:1:-1].ljust(32,'0'),2)
# @lc code=end