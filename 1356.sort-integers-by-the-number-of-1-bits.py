#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = list(map(lambda v: bin(v)[2:], arr))
        arr.sort(key=lambda v: int('0b'+v,2))
        arr.sort(key=lambda v: v.count('1'))
        arr = list(map(lambda v: int('0b'+v,2), arr))
        return arr

# @lc code=end

