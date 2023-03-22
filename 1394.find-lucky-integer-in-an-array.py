#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqHash = {}

        for n in arr:
            if not n in freqHash:
                freqHash[n] = 0
            freqHash[n] += 1

        lucky = -1
        for k,v in freqHash.items():
            if k==v and k > lucky:
                lucky = k
        return lucky

# @lc code=end

