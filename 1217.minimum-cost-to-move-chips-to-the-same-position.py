#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Minimum Cost to Move Chips to The Same Position
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # min of sum odds / sum events
        odds = len([x for x in position if x%2])
        evens = len([x for x in position if not x%2])
        return min(odds, evens)
# @lc code=end

