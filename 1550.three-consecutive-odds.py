#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len (arr) < 3: return False

        for i in range(2, len(arr)):
            if arr[i]%2 and arr[i-1]%2 and arr[i-2]%2:
                return True
        return False
# @lc code=end

