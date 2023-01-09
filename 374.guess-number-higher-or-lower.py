#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import math
class Solution:
    def guessNumber(self, n: int) -> int:
        global guess

        bot = 0
        top = n
        check = math.ceil(top / 2)
        resp = guess(check)

        while resp != 0:
            if resp == -1:
                top = check
            elif resp == 1:
                bot = check

            check = bot + math.ceil((top - bot) / 2)
            resp = guess(check)

        return check
# @lc code=end

