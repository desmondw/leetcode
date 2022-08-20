#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        carry = 1
        for i, d in enumerate(digits[::-1]):
            d += carry
            carry = d // 10
            digits[length-1-i] = d % 10
        return ([carry] if carry else []) + digits
# @lc code=end

