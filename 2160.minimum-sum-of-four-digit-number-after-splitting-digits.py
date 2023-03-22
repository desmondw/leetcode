#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        opts = [
            self.serialize(num,1),
            self.serialize(num,2),
            self.serialize(num,3),
        ]
        return min(opts)

    def serialize(self, n, a):
        n = str(n)
        x = self.getLowest(n[:a])
        y = self.getLowest(n[a:])
        if a == 2:
            z = self.getLowest(n[0]+n[3])
            v = self.getLowest(n[1:3])
            return min(x+y, z+v)
        return x+y

    def getLowest(self, n):
        if len(n) == 1: return int(n)
        if len(n) == 2: return min(int(n), int(n[1]+n[0]))
        opts = [
            int(n),
            int(n[0]+n[2]+n[1]),
            int(n[1]+n[0]+n[2]),
            int(n[1]+n[2]+n[0]),
            int(n[2]+n[0]+n[1]),
            int(n[::-1]),
        ]
        return min(opts)
# @lc code=end

