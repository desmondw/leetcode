#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = hash.get(num, []) + [i]

        print(hash)

        for num, idxs in hash.items():
            if len(idxs) > 1:
                idxs.sort()
                for i in range(0,len(idxs)-1):
                    if abs(idxs[i] - idxs[i+1]) <= k: return True

        return False
# @lc code=end

