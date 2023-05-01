#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start
import math
class Solution:
    def isThree(self, n: int) -> bool:
        if n < 3: return False
        found = False
        for p in range(2,10**4):
            print(f'{n} % {p} = ',n%p)
            if p > n / 2: return found
            if n % p == 0:
                if found: return False
                found = True
        return found
# @lc code=end

