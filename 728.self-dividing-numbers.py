#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right+1):
            if self.divisible(i):
                nums.append(i)
        return nums

    def divisible(self, num):
        for i in list(str(num)):
            if i == '0' or num % int(i):
                return False
        return True
# @lc code=end

