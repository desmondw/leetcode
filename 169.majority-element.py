#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num not in hash: hash[num] = 0
            hash[num] += 1
        return sorted(hash.items(), key=lambda kv: kv[1])[-1][0]
# @lc code=end

