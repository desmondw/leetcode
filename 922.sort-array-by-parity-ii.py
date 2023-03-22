#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = {}
        iEven = 0
        iOdd = 1
        for num in nums:
            if num%2==1:
                result[iOdd] = num
                iOdd += 2
            else:
                result[iEven] = num
                iEven += 2
        return [result[i] for i in sorted(result.keys())]
# @lc code=end

