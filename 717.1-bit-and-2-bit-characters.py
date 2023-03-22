#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        carry = ''
        for bit in bits[:-1]:
            carry += str(bit)
            if len(carry) == 2 or carry == '0':
                carry = ''
        return not len(carry)

# @lc code=end

