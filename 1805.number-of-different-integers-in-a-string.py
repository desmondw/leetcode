#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
import re
import functools
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = re.split('\D+', word)
        if nums[0] == '':  nums = nums[1:]
        if nums[-1] == '': nums = nums[:-1]
        nums = map(lambda v: int(v), nums)
        nums = set(nums)
        return len(nums)
# @lc code=end

