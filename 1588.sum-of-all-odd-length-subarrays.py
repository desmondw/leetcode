#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        for size in range(3,len(arr)+1,2):
            for i in range(0,len(arr)-size+1):
                total += sum(arr[i:i+size])
        return total
# @lc code=end

