#
# @lc app=leetcode id=2396 lang=python3
#
# [2396] Strictly Palindromic Number
#

# @lc code=start
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            based = self.numberToBase(n, i)
            print(i, based, based[::-1], based == based[::-1])
            if based != based[::-1]:
                return False
        return True

    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
# @lc code=end

