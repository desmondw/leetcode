#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [str(bin(i)).count('1') for i in range(0,n+1)]
# @lc code=end

