#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
import functools
class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash = {}
        top = 0
        for i in range(1, n+1):
            arr = list(str(i))
            sum = functools.reduce(lambda a,v: a+int(v), arr, 0)
            if sum not in hash: hash[sum] = 0
            hash[sum] += 1
            if hash[sum] > top: top = hash[sum]

        return len([x for x in list(hash.values()) if x == top])

# @lc code=end

