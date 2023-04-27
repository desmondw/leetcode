#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a in arr1:
            myFilter = filter(lambda b: abs(a-b) <= d, arr2)
            count += int(not bool(len(list(myFilter))))
        return count
# @lc code=end

