#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        code = code[:]*3
        result = code[:]
        for i in range(length, length*2):
            if k > 0:
                result[i] = sum(code[i+1:i+1+k])
            elif k < 0:
                result[i] = sum(code[i+k:i])
            else:
                result[i] = 0

        return result[length:length*2]
# @lc code=end

