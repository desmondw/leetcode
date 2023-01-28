#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        i = 1
        end = len(nums)
        hasModified = False

        while i < end:
            if nums[i-1] >= nums[i]:
                if hasModified:
                    return False
                else:
                    hasModified = True

                    # which to remove?
                    if i+1 == end or nums[i-1] < nums[i+1]:
                        nums.pop(i)
                    elif i == 1 or nums[i-2] < nums[i]:
                        nums.pop(i-1)
                    else:
                        return False

                    i -= 1
                    end -= 1
            i += 1
        return True

# @lc code=end

