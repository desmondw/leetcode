#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'

        # convert to reverse number array
        n1 = list(map(lambda v: int(v), list(num1)[::-1]))
        n2 = list(map(lambda v: int(v), list(num2)[::-1]))
        n3 = []

        # multiplication phase
        for i, a in enumerate(n1):
            for j, b in enumerate(n2):
                k = i + j
                c = a * b

                while len(n3) <= k:
                    n3.append(0)
                n3[k] += c

        # addition phase
        i=0
        while i < len(n3):
            carry = int(n3[i] / 10)
            n3[i] %= 10
            if carry:
                if i+1 == len(n3):
                    n3.append(0)
                n3[i+1] += carry

            i += 1

        # convert back to string
        result = ''.join(list(map(lambda v: str(v), n3[::-1])))
        return result

# @lc code=end

