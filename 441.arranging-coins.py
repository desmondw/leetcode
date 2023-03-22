#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        while n > rows:
            rows += 1
            n -= rows
        return rows + int(rows < n)
# @lc code=end

