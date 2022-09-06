#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return len(bits)<2 or bits[-2] == bits[-1] == 0
        # num = int(''.join(str(bits)[1:-1].split(', ')), 2)
        # print(num)

        # if num % 2 == 0:
        #     return False
        # return True

# @lc code=end

