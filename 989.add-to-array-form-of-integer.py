#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(x) for x in num]))
        result = list(str(num + k))
        return [int(x) for x in result]

    # def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    #     num = num[::-1]
    #     k = [int(v) for v in str(k)][::-1]

    #     result = self.addArr(num, k)[::-1]
    #     while result[0] == 0:
    #         result.pop(0)
    #     return result

    # def addArr(self, a, b, carry=0):
    #     if len(a) == 0 and len(b) == 0 and carry == 0:
    #         return [0]

    #     ad = a[0] if len(a) else 0
    #     bd = b[0] if len(b) else 0

    #     sum = ad + bd + carry
    #     carry = int(sum / 10)
    #     sum %= 10

    #     return [sum] + self.addArr(a[1:], b[1:], carry)
# @lc code=end

