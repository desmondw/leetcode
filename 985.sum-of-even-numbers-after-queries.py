#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start
import functools
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum = functools.reduce(lambda a,v: a+v if v%2==0 else a, nums, 0)
        print('initial sum', sum)

        for val, index in queries:
            print(val, index)
            if nums[index] % 2 == 0: sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0: sum += nums[index]
            result.append(sum)
            print('sum', sum)

        return result
# @lc code=end

