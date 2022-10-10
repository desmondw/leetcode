#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        counts = [0, 1]
        for i in range(2, n+1):
            counts.append(counts[0] + counts[1])
            counts.pop(0)
        return counts[1]

# @lc code=end

